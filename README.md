# Dev Test Branch (09/27/22)

## What's New?
This is the first iteration of the Development Test Branch! This branch is dedicated to experimental changes before they are pushed to the main branch. 
Some of the changes to this iteration are:
* Seperated and created more Menu classes for the Edit Game screen
* Added functionality for the Menu classes above
* Added foundation for database connectivity
* ... and more

**MAJOR BUGS ARE TO BE EXPECTED**

Be sure to check the new Dependency Installation


## Basics
* Initial version of University of Arkansas CSCE 3513 Team Project - Laser Tag program
* Intended only for use in Team 8 of UArk CSCE 3513, Fall 2022
* Program is incomplete. Major bugs are to be expected
* Program has currently only been tested on Windows 10 and Linux Cinnamon Mint so far
* Program requires latest pynput and tkinter modules to be installed
* Program is NOT intended to work on Mac OS

## Dependency Installation
* Tkinter should be installed with python3 by default
* If not installed on linux, use command: sudo apt-get install python-tk
* [Devtest] Download github devtest repository, either using Git or download ZIP file. Unpack somewhere on your computer and go into the directory in commandline: cd (full directory path)
* [Devtest] Set up a virtual environment for python: python -m venv (name of directory here)
* [Devtest] Activate the virtual environment in CLI: (name of directory)\scripts\activate
* [Devtest] Install dependencies using pip: pip install -r requirements.txt. If the command fails, try the below instead.
* For pynput, install via pip: pip install pynput
* [Devtest] New dependency - psycopg2. Install using pip: pip install psycopg2-binary
* [Devtest] Set the database url in your virtual environment. On windows: set DATABASE_URL=databasetokenhere . On Linux: export DATABASE_URL=databasetokenhere .

## How to
* Run program by typing in commandline (without quotations): "python main.py"
* [Devtest] Use F5 to change between screens, including Splash
* Only the Edit Game screen has functionality as of now
* Edit Game functionality uses arrow keys, and Ins/Del as seen on the bottom part of the window

## Testing Needed
* More systems (test with multiple Windows/Linux computers)
* [Devtest] Ensure screen resolution is not an issue (current minimum: 1000x700)
* ... (More to be added)
