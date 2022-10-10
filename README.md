# Main Branch (10/09/22)

## What's New?
Some of the changes to this iteration are:
* Fixed previous codename found not showing in UI
* Harded database url into code
* Fixed error during transition to Play Game screen

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
* Download github devtest repository, either cloning by using Git or download ZIP file. Unpack somewhere on your computer and go into the directory in commandline: cd (full directory path)
* (Optional) Set up a virtual environment for python: python -m venv (name of directory here)
  * (Linux): If virtual environment addon for python is not installed by default and gives an error, try either "sudo apt install python3.8-venv" or "apt install python3.8-venv", without quotations
* (Optional) Activate the virtual environment in CLI: 
  * (Windows): (name of directory)\scripts\activate
  * (Linux): source (name of directory)/bin/activate
* Install dependencies using pip: pip install -r requirements.txt. If the command fails, try the below instead.
  * For pynput, install via pip: pip install pynput
  * For psycopg2, install using pip as well: pip install psycopg2-binary
 
## Database Token, Security, and Information
* The database token (usually called database url or URI)  may expire after a certain time outside our control unfortuanately. This is mentioned by Heroku that it will change periodically automatically. If for whatever reason it expires, please email myself (ctj011@uark.edu) or one of the other team members to update the code so that the database works properly.
* Previously, any user downloading this program would have to set an environment variable, DATABASE_URL, in order to communicate between the database and the program. The variable would be set to the database url/URI/database token, previously given in this readme. While this would help prevent having to update the code each time by having the user instead send a request for the database url/URI itself, this has been changed for the sake of the grader. As mentioned in the next point, it has been removed and harded after asking the professor for ease-of-access.
* Regarding security: The database token / database url would normally not be shared on a public website such as GitHub; however, by the request of the professor for ease-of-access sake, and since this is an academic learning environment, it is included in the Database.py file. It is intended that only the graders and students access the database.

## How to
* Run program by typing in commandline (without quotations): "python main.py"
* Wait for splash screen (3 seconds) to take you to Edit Game screen
* Only the Edit Game screen has functionality as of now:
  * Use Arrow keys to move up/down the player list
  * Insert a player using Ins key, Delete a player using Del key (as seen as bottom of window)
  * Press F7 to delete table database (this is for debugging, will likely not be in final version)
  * Press F5 to move to Play Screen. The Play Screen has no functionality and as such, this will be the last screen you see before closing the Tkinter window.

## Testing Needed
* More systems (test with multiple Windows/Linux computers)
* Ensure screen resolution is not an issue (current minimum: 1000x700)
* ... (More to be added)
