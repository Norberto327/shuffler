##### SHUFFLER.PY ###########################################
# Made by Norberto327
# Github repository of this program: Norberto327/shuffler
# Link: https://github.com/Norberto327/shuffler/
# Licensed under the GNU general public license (GPL). You may copy, modify,
# and distribute this software freely, but no warranty is provided to the user.
# More info in the LICENSE file of the github repository.
# 
# WARNING:
# For the program to work, it MUST be placed in a directory with 2 folders in it
# and nothing else. Otherwise it will not work. The program may be modified to
# only read two folders with predetermined names by changing mainDir (line 37)
# to a list with the names of the folders. In any case, the script must be
# located in the same directory as the target folders.
# 
# ABOUT:
# This program reads two folders in the same directory, pairs one file from one
# directory with another file from another directory randomly, with no repeats.
# Then it creates a new folder. In it, more folders, with each folder containing
# one pairing of files.
# If there is a folder with more files than the other one, the files in the
# shorter folder will repeat and appear in multiple pairings.
# If the amount of files in the longer folder is a multiple of the number of
# files in the shorter one, then the files in the shorter folder will appear
# equally throughout the pairings. Otherwise, some files from the shorter
# directory will appear in 1 less pairing than other files (depends on the
# remainder).
# 
# By the way, if you don't want to see the messages (useful for debugging),
# uncomment all the lines with #DB at the end of them.
#
########## START OF THE CODE ##########################################
# Import needed libs
import os, shutil # For handling files and folders 
import random # For randomising
mainDirPath = os.path.abspath(os.path.dirname(__file__)) # Directory with file and folders
mainDir = os.listdir(mainDirPath) # List of directories
mainDir.remove(os.path.basename(__file__)) # Removes this file from the list

originalMainDir = mainDir # For renaming back to original

# Make sure that there are 2 dirs,
# If not it shows an error and exits
if len(mainDir) != 2:
    raise Exception("Directory contains " + str(len(mainDir)) + " folders, 2 required.")
    exit()
else:
    pass

print("Path:", mainDirPath)
print("Detected directories:", mainDir) #DB

# Rename dirs for easier handling 
os.rename(mainDir[0], "dir1")
mainDir[0] = "dir1"
os.rename(mainDir[1], "dir2")
mainDir[1] = "dir2"

    
# Make dir lists
dir1 = os.listdir(mainDirPath+"/dir1")
dir2 = os.listdir(mainDirPath+"/dir2")

print(originalMainDir[0]+":", dir1) #DB
print(originalMainDir[1]+":", dir2) #DB

# Define longer and shorter lists
if len(dir1) < len(dir2):
    longerDir = dir2
    shorterDir = dir1
else:
    longerDir = dir1
    shorterDir = dir2

dir1 = tuple(dir1)
dir2 = tuple(dir2)
pairings = []
print("Pairings: ") #DB
### Main loop ########################
while longerDir != []:
    for x in range(0, len(shorterDir)):
        if longerDir == []:
            break
        pairing = random.randint(0, len(longerDir)-1)
        pairings.append((shorterDir[x], longerDir[pairing]))
        print(shorterDir[x], longerDir[pairing]) #DB
        del longerDir[pairing]

print("Pairings:", pairings) #DB

pairingPath = mainDirPath + "/pairings"
os.mkdir(pairingPath)
print("Path to pairing folder:", pairingPath) #DB

# Define longer and shorter lists... again
print(dir1) #DB
print(dir2) #DB
if len(dir1) < len(dir2):
    longerDir = dir2
    shorterDir = dir1
elif len(dir1) > len(dir2):
    longerDir = dir1
    shorterDir = dir2

for x in range(len(pairings)):
    pathToPairing = pairingPath + "/pairing" + str(x)
    os.mkdir(pathToPairing)
    a, b = pairings[x]
    if len(dir1) < len(dir2):
        indexA = dir1.index(a)
        indexB = dir2.index(b)
        shutil.copy2(mainDirPath+"/dir1/"+shorterDir[indexA], pathToPairing)
        shutil.copy2(mainDirPath+"/dir2/"+longerDir[indexA], pathToPairing)
    else:
        indexA = dir2.index(a)
        indexB = dir1.index(b)
        shutil.copy2(mainDirPath+"/dir2/"+shorterDir[indexA], pathToPairing)
        shutil.copy2(mainDirPath+"/dir1/"+longerDir[indexA], pathToPairing)
        

os.rename(mainDir[0], originalMainDir[0])
os.rename(mainDir[1], originalMainDir[1])