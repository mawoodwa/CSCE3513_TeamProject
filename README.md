# Main Branch (10/06/22)

## What's New?
Some of the changes to this iteration are:
* Added 3 second splash screen
* Changed Database to work correctly with main Heroku repository
* Move To Play Screen confirmation menu
* ... and more

**MAJOR BUGS ARE TO BE EXPECTED**

Be sure to check the Dependency Installation


## Basics
* 2nd devtest version of University of Arkansas CSCE 3513 Team Project - Laser Tag program
* Intended only for use in Team 8 of UArk CSCE 3513, Fall 2022
* Program is incomplete. Major bugs are to be expected
* Program has currently only been tested on Windows 10 and Ubuntu (Linux Cinnamon Mint) so far
* Program requires latest pynput, psycopg2-binary, and tkinter modules to be installed
* Program is NOT intended to work on Mac OS

## Dependency Installation
* Tkinter should be installed with python3 by default
  * If not installed on linux by default, try the following command: sudo apt-get install python-tk
* Download github devtest repository, either using Git or download ZIP file. Unpack somewhere on your computer and go into the directory in commandline: cd (full directory path)
* (Optional) Set up a virtual environment for python: python -m venv (name of directory here)
  * (Linux): If virtual environment addon for python is not installed by default and gives an error, try either "sudo apt install python3.8-venv" or "apt install python3.8-venv", without quotations
* (Optional) Activate the virtual environment in CLI: 
  * (Windows): (name of directory)\scripts\activate
  * (Linux): source (name of directory)/bin/activate
* Install dependencies using pip: pip install -r requirements.txt. If the command fails, try the below instead.
  * For pynput, install via pip: pip install pynput
  * New dependency - psycopg2. Install using pip: pip install psycopg2-binary
* Set the database url in your virtual environment. 
  * (Windows): set DATABASE_URL=databasetokenhere . 
  * (Linux): export DATABASE_URL=databasetokenhere .

## How to
* Run program by typing in commandline (without quotations): "python main.py"
* Wait for splash screen (3 seconds) to take you to Edit Game screen
* Only the Edit Game screen has functionality as of now:
  * Use Arrow keys to move up/down the player list
  * Insert a player using Ins key, Delete a player using Del key (as seen as bottom of window)
  * Press F7 to delete table database (this is for debugging, will likely not be in final version)
  * Press F1 to move to Play Screen. The Play Screen has no functionality and as such, this will be the last screen you see before closing the Tkinter window.

## Testing Needed
* More systems (test with multiple Windows/Linux computers)
* Ensure screen resolution is not an issue (current minimum: 1000x700)
* ... (More to be added)
