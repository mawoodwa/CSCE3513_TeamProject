import socket
import threading

class Network:
    def __init__(self):
        self.boolHasStarted = False
        self.boolHasNewTransmission = False
        self.queueLastTransmissions = ""
        self.setupUDP()
        
    def setupUDP(self):
        print("Setting up UDP socket")
        self.udp_IP = "127.0.0.1" # localhost
        self.udp_PORT_BROAD = 7500
        self.udp_PORT_REC = 7501
        self.udp_socket_Rec = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udp_socket_Rec.bind((self.udp_IP, self.udp_PORT_REC))
        print("Finished setting up UDP receiving socket: {}:{}".format(self.udp_IP, self.udp_PORT_REC))
        self.udp_socket_Broad = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udp_socket_Broad.bind((self.udp_IP, self.udp_PORT_BROAD))
        print("Finished setting up UDP broadcasting socket: {}:{}".format(self.udp_IP, self.udp_PORT_BROAD))
        
    def getBroadcastingSocket(self):
        return self.udp_socket_Broad
        
    def getReceivingSocket(self):
        return self.udp_socket_Rec
        
    def startThread(self):
        print("Starting network listening thread...")
        self.boolHasStarted = True
        self.thread_UDP = threading.Thread(target=self.methodThread_LoopUDP, args=(), daemon=True)
        self.thread_UDP.start()
        
    def hasNewTransmission(self):
        return self.boolHasNewTransmission
        
    def getLastTransmission(self):
        self.boolHasNewTransmission = False
        return self.strLastTransmission
        
    def methodThread_LoopUDP(self):
        while True:
            self.receiveUDP()
            strPlayerHit = self.getPlayerHit(self.strLastTransmission)
            if strPlayerHit != None:
                self.broadcastUDP(strPlayerHit)
        
    def receiveUDP(self):
        udpData, udpAddress = self.udp_socket_Rec.recvfrom(1024)
        #print("Received from {}: {}".format(udpAddress, udpData))
        self.strLastTransmission = udpData.decode()
        #print("\tFormatted data: {}".format(self.strLastTransmission))
        self.boolHasNewTransmission = True
            
    def getPlayerHit(self, transmission):
        listDataSplit = transmission.split(":")
        if len(listDataSplit) > 1:
            return listDataSplit[1]
        return None
        
    def broadcastUDP(self, strIDPlayerHit):
        udpData = str(strIDPlayerHit).encode() # Ensure str format
        #print("Broadcasting to {}:{}: {}".format(self.udp_IP, self.udp_PORT_BROAD, udpData))
        self.udp_socket_Broad.sendto(udpData, (self.udp_IP, self.udp_PORT_BROAD))