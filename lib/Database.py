import os
import psycopg2

class Database():
    def __init__(self):
        print("Initializing Database Object...")
        self.conn = None
        self.cursor = None
        self.strSelectedTable = "player"
        
    def openConnection(self):
        try:
            self.connectUsingVenv()
            print(self.conn)
            self.cursor = self.conn.cursor()
            print(self.cursor)
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error:")
            print(error)
            
    def connectUsingVenv(self):
        # DATABASE_URL = os.environ['DATABASE_URL']
        DATABASE_URL = "postgres://afnatpikeuzgvb:b9929e6440f676fdb770c4962b288c7b6d284d74e670c87c0d064f8b11d9bc2d@ec2-34-195-163-197.compute-1.amazonaws.com:5432/dd30p75admf175"
        print(DATABASE_URL)
        self.conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    
    def connectUsingCode(self):
        self.conn = psycopg2.connect(database="db_username",
                                host="db_host",
                                user="db_user",
                                password="db_pass",
                                port="db_port",
                                keepalives=1,
                                keepalives_idle=30,
                                keepalives_interval=10,
                                keepalives_count=5)
                                
    def selectTable(self, strTableName):
        self.strSelectedTable = strTableName
                                
    def getAllTables(self):
        self.cursor.execute("""
        SELECT * FROM information_schema.tables WHERE table_schema='public';""")
        return self.cursor.fetchall()
    
    def getAllRows(self):
        try:
            self.cursor.execute("SELECT * FROM {table} ORDER BY id".format(table=self.strSelectedTable))
            rows = self.cursor.fetchall()
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error:")
            print(error)
            return None
            
    def deleteById(self,id):
        try:
            data=[id]
            self.cursor.execute("DELETE FROM {table} WHERE id=%s RETURNING *".format(table=self.strSelectedTable), data)
            rows = self.cursor.fetchall()
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error:")
            print(error)
            return None
            
    def getLastId(self):
        try:
            self.cursor.execute("""
            SELECT id, first_name, last_name, codename 
            FROM {table} ORDER BY id DESC LIMIT 1""".format(table=self.strSelectedTable));
            rows = self.cursor.fetchall()
            return rows
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error:")
            print(error)
            return None
            
    def findId(self, id):
        data = [id]
        self.cursor.execute("""
        SELECT * FROM {table} WHERE id=%s;""".format(table=self.strSelectedTable),data)
        return self.cursor.fetchall()
            
    def updateUsingId(self, listPlayerInfo):
        if self.isPlayerInfoValid(listPlayerInfo):
            data=[listPlayerInfo[1], listPlayerInfo[2], listPlayerInfo[3], listPlayerInfo[0]]
            self.cursor.execute("""
            UPDATE {table} 
            SET first_name=%s, last_name=%s, codename=%s WHERE id=%s;
            """.format(table=self.strSelectedTable), data)
        else:
            print("Error: listPlayerInfo is incorrect size. Cannot add to DB")
            
    def deleteAllRows(self):
        self.cursor.execute("DELETE FROM {table};".format(table=self.strSelectedTable))
            
    def isPlayerInfoValid(self, listPlayerInfo):
        isListSizeValid = len(listPlayerInfo) == 4
        if isListSizeValid:
            isTypeValid = type(listPlayerInfo[0]) is int and type(listPlayerInfo[1]) is str and type(listPlayerInfo[2]) is str and type(listPlayerInfo[3]) is str
            if isTypeValid:
                isStrSizeValid = len(listPlayerInfo[1]) <= 30 and len(listPlayerInfo[2]) <= 30 and len(listPlayerInfo[3]) <= 30
                return isStrSizeValid
            return False
        return False
        
    def findPlayerByName(self,firstName, lastName):
        data = (firstName.upper(), lastName.upper())
        self.cursor.execute("""
        SELECT person.id, person.first_name, person.last_name, person.codename
        FROM {table} AS person
            INNER JOIN {table} AS returnValue
            ON UPPER(person.first_name) = %s
            AND UPPER(person.last_name) = %s
        GROUP BY person.id, person.first_name, person.last_name, person.codename
        ORDER BY person.id, person.first_name, person.last_name, person.codename""".format(table=self.strSelectedTable), data)
        return self.cursor.fetchall()
            
    def insertPlayer(self, listPlayerInfo):
        if self.isPlayerInfoValid(listPlayerInfo):
            self.cursor.execute("""
            INSERT INTO {table} (id, first_name, last_name, codename) VALUES (%s, %s, %s, %s);""".format(table=self.strSelectedTable), listPlayerInfo)
        else:
            print("Error: listPlayerInfo is incorrect size. Cannot add to DB")
            
    def commit(self):
        if self.conn is not None:
            self.conn.commit()
    
    def closeDB_NoCommit(self):
        if self.conn is not None:
            self.cursor.close()
            self.conn.close()
    
    def closeDB_Commit(self):
        if self.conn is not None:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
    