#MultiTerminal Database Installer Script for Linux x86_64 by Undo Technologies/Brennan LeBlanc
#Copyright 2019 Brennan LeBlanc and Undo Technologies

import os #This allows us to create folders for MultiTerminal installation process
import time
import git

path = "./database"
verify_yes = "yes", "Yes", "YES", "y", "Y"

print("MultiTerminal Database Installer - UndoTechnologies")
print("Version 1.0.0")
time.sleep(2)
print("For use with MultiTerminal Version 0.0.1a and up.")
time.sleep(2)
print("Please make sure this script was ran with 'Super User (su)' or 'sudo' privilges and that this script is in the your 'MultiTerminal Directory'")
time.sleep(3)
os.system("clear")
print("Welcome to the MultiTerminal installation process. Here we will download critical files for the operation of MultiTerminal")
print("PLEASE NOTE: This process will require access to the internet to download files from our repository. It will also create a new folder as well")
input("After reading, press enter to continue...")
os.system("clear")
print("Here is the list of operations...")
print("1. Create a new folder in the current directory")
print("2. Download files for MultiTerminal in the new directory")
print("That's it! There is nothing else you need to do!")
input("Please read carefully and press enter to continue...")
os.system("clear")
print("Alright! We will now begin the installation process!")
print("Before we begin we must ask this:")
verify = input("Are you sure you want to install the MultiTerminal Database to your system? Please note that you assume all risks by saying Yes to this and understand that you may lose data if these directory's already exist! Would you like to continue? (Yes/No) > ")
if verify in verify_yes:
	os.system("clear")
	print("Alright! Now creating new database directory...")
	os.mkdir(path)
	time.sleep(5)
	print("Directory created! Now downloading database...")
	git.Git(path).clone("https://github.com/UndoTechnologies/MultiTerminalDatabase.git")
	time.sleep(5)
	os.system("clear")
	print("Everything is done on my end! If any errors have occurred, please refer to the troubleshooting document that came with this installer or contact Undo Technologies!")
	print("Thank you for using the MultiTerminal Database installer! Be sure to run this every 1-2 weeks as new updates may be out!")
	input("Press enter to exit...")
else:
	os.system("clear")
	print("Ok... fair note that MultiTerminal will NOT work as intended, unless you already installed the database and opened this by accident.")
	print("If you already have the Database installed, make sure to keep it up to date!")
	print("New Database updates come out every 1-2 weeks so come back often!")
	input("Alright, that's all from me! Thank you for taking interest in MultiTerminal! Please press enter to exit...")
