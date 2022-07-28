# shuffler.py
Made by Norberto Arteaga Cecys
Github: Norberto327
Github repository of this program: Norberto327/shuffler
Link: https://github.com/Norberto327/shuffler/

Licensed under the GNU general public license (GPL)
You may copy, modify, and distribute this software freely, but no warranty is provided to the user.
More info in the LICENSE file of the github repository.

# WARNING:
For the program to work, it MUST be placed in a directory with 2 folders in it and nothing else.
Otherwise it will not work. The program may be modified to only read two folders with predetermined
names by changing mainDir (line 26) to a list with the names of the folders and
In any case, the script must be located in the same directory as the target folders.

# ABOUT:
This program reads two folders in the same directory, pairs one file from one directory with
another file from another directory randomly, with no repeats. Then it creates a new folder.
In it, more folders, with each folder containing one pairing of files.

If there is a folder with more files than the other one, the files in the shorter folder will repeat
and appear in multiple pairings.

If the amount of files in the longer folder is a multiple of the number of files in the shorter one,
then the files in the shorter folder will appear equally throughout the pairings. Otherwise, some
files from the shorter directory will appear in 1 less pairing than other files (depends on the remainder).

By the way, if you don't want to see the messages, uncomment all the lines with #DB at the end of them.
