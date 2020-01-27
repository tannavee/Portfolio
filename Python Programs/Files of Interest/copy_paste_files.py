import shutil
import os

txtFilePath = input("Enter text file path") # select the text file
sourcePath = input("Enter source directory path") # select the source directory
destPath = input("Enter destination direcoty path") # select the destination directory

# create empty list
filesToFind = []

# read all the file names from the text file
with open(txtFilePath, "r") as txtFile:
    # going line by line
    for row in txtFile:
        # adding file names in the empty list
        filesToFind.append(row.strip())
print(filesToFind)

for fileName in os.listdir(sourcePath):
    if filename in filesToFind:
        filename = os.path.join(sourcePath, filename)
        shutil.copy(fileName, destPath)
print("Matching files have been copied")

