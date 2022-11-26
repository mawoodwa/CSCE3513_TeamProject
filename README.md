# Devtest Branch (11/25/22)

## What's New?
Some of the changes to this iteration are:

* Finishing requirements for Sprint 4 (11/15/22)
  * Added Network.py to manage broadcasting/receiving from localhost on ports 7500 and 7501.
  * Modified GameAction to be able to dynamically push events, as well as modified GameAction aesthetics.
  * Updated Play Game screen to be able to generate network IDs and dispatch to Scoreboard.
  * Modified Scoreboard to accommodate network IDs, as well as add score to a player based on ID, sort the player based on score, and update team score.
  * Added TrafficGenerator.py to dynamically create events and broadcast to localhost port 7501 (press f4 on Play Game screen to start traffic generator).
* Update (11/20/22)
  * Updated Database for offline support. This is done by using SQLite.
    * If connection to Heroku fails for whatever reason, the program will attempt to open db\database.db if it exists. If it does not exist, the program will create it. Any updates to the DB will be written to this new offline DB instead. The offline DB does not interact with the online DB in any way other than acting as an alternative for when Heroku's free database comes offline on 11/28/22.
  * Added flashing team scores.
    * If both team scores are the same, neither team flashes. If one is higher than the higher, the team score will alternate between 2 colors every 0.25 seconds, flashing every 0.5 seconds
    * Currently, green team's 2 colors are very close to eachother and will need to be adjusted. It is difficult to tell when it is flashing.
  * Updated program to ignore invalid ID's received from localhost. This should fix the previous issue where an invalid ID using the professor's traffic generator would cause the program to crash.
* Update (11/25/22)
  * Edit Game screen now prompts user for ID rather than first/last name
    * Every new player entry is now only concerned with ID/codename. Team asked professor on Tuesday and it sounds like first/last name is not required but a custom user input for ID/codename is. ID was previously auto-generated, now user input instead.
    * Every new player entry will list "(blank)" in place of first/last name so that the Heroku database/python Database wrapper class does not need to be remade/altered.
    * New IDs can range from 0 - 99,999.
    * Game will prevent operator from entering in a player if their ID is already on the board. This is to prevent ID conflicts during the networking portion on the "Play Game" screen.
  * Green team score on "Play Game" screen will flash a mid-cyan color if they have the highest team score.
  
* **LIMITATIONS AND OTHER INFORMATION**
  * Wait Timer reduced to 5 seconds for debugging

**MAJOR BUGS ARE TO BE EXPECTED**

Be sure to check the Dependency Installation

## Basics
* Intended only for use in Team 8 of UArk CSCE 3513, Fall 2022
* Program is incomplete. Major bugs are to be expected
* Program has currently only been tested on Windows 10 and Ubuntu (Linux Cinnamon Mint) so far
* Program requires latest pynput, psycopg2-binary, and tkinter modules to be installed
* Program is NOT intended to work on Mac OS

## Dependency Installation
* Tkinter should be installed with python3 by default
  * If not installed on linux by default, try the following command: sudo apt-get install python-tk
* Download github main branch repository, either cloning by using Git or download ZIP file. Unpack somewhere on your computer and go into the directory in commandline: cd (full directory path)
* (Optional) Set up a virtual environment for python: python -m venv (name of directory here)
  * (Linux): If virtual environment addon for python is not installed by default and gives an error, try either "sudo apt install python3.8-venv" or "apt install python3.8-venv", without quotations
* (Optional) Activate the virtual environment in CLI: 
  * (Windows): (name of directory)\scripts\activate
  * (Linux): source (name of directory)/bin/activate
* Install dependencies using pip: pip install -r requirements.txt. If the command fails, try the below instead.
  * For pynput, install via pip: pip install pynput
  * For psycopg2, install using pip as well: pip install psycopg2-binary
  
## How to
* Run program by typing in commandline (without quotations): "python main.py"
* Wait for splash screen (3 seconds) to take you to Edit Game screen
* On the Edit Game screen:
  * Use Arrow keys to move up/down the player list
  * Insert a player using Ins key, Delete a player using Del key (as seen as bottom of window)
  * Press F7 to delete table database (this is for debugging, will likely not be in final version)
  * Press F5 to move to Play Screen.
* On the Play Game screen:
  * Currently, only F5 key has functionality other than the timers, allowing you to pause/unpause game countdown/warning timer and switch back to Edit Game screen.
 
## Database Token, Security, and Information
* The database token (usually called database url or URI)  may expire after a certain time outside our control unfortuanately. This is mentioned by Heroku that it will change periodically automatically. If for whatever reason it expires, please email myself (ctj011@uark.edu) or one of the other team members to update the code so that the database works properly.
* Previously, any user downloading this program would have to set an environment variable, DATABASE_URL, in order to communicate between the database and the program. The variable would be set to the database url/URI/database token, previously given in this readme. While this would help prevent having to update the code each time by having the user instead send a request for the database url/URI itself, this has been changed for the sake of the grader. As mentioned in the next point, it has been removed and hardcoded after asking the professor for ease-of-access.
* Regarding security: The database token / database url would normally not be shared on a public website such as GitHub; however, by the request of the professor for ease-of-access sake, and since this is an academic learning environment, it is included in the Database.py file. It is intended that only the graders and students access the database.

## Testing Needed
* More systems (test with multiple Windows/Linux computers)
* Ensure screen resolution is not an issue (current minimum: 1000x700)
* ... (More to be added)
