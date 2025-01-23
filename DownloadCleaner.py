import os
import shutil
from pathlib import Path


class Downloads:

    rootDir = str(Path.home()) + "/Downloads"


    def __init__(self):
        self.fileList = []
        self.folderDictionary = {}


    def listFileTypes(self):
        suffixList = []
        for file in os.listdir(self.rootDir):
            reversedSuffix = ""
            suffix = ""
            if(file[-1] != "." and "." in file):
            #if the file contains a suffix, then the suffix is added to a string in reverse order
                index = -1
                while file[index] != ".":
                    reversedSuffix += file[index]
                    index -= 1
                reversedSuffix += "."

            #reversing the suffix to it's normal form

            for i in range(len(reversedSuffix)):
                suffix += reversedSuffix[-i - 1]
            
            if suffix != "":
                suffixList.append(suffix)
        
        print(suffixList)
        for i in range(len(suffixList)):
            if i == len(suffixList) - 1:
                print(suffixList[i])
            else:
                print(suffixList[i], end = ", ")
                
        
    def createDictionary(self):
        
            
        folderName = input("Enter the name of a folder: ") #Loops over however many folders the user chooses
        while folderName != "q":
            fileType = input("Enter the file type you would like to store in this folder: ")
            while fileType != "q":
                if folderName not in self.folderDictionary: #This statement checks to see if you are adding more than one value to a single key
                    self.fileList.append(fileType) #These statements create a new key (file name) and adds the value
                    self.folderDictionary[folderName] = self.fileList 
                else:
                    self.folderDictionary[folderName].append(fileType) #This statement adds a file type to the list of an already existing folder
                fileType = input("Enter the file type you would like to store in this folder (q to quit): ") #These next few lines of code do the same thing as previous lines but allows the user to quit
                if fileType != "q":
                    if folderName not in self.folderDictionary:
                        self.fileList.append(fileType)
                        self.folderDictionary[folderName] = self.fileList
                    else:
                        self.folderDictionary[folderName].append(fileType)
                    fileType = input("Enter the file type you would like to store in this folder (q to quit): ")

                self.fileList = [] #This statement empties the list for the next folder
                

            
            folderName = input("Enter the name of a folder (q to quit): ")
            
        

    
    def createFolder(self):
        for key in self.folderDictionary: #Loops through all folders given by user
            newFolder = os.path.join(self.rootDir, key) #Creates a directory path for folder
            try: #This will add the folder if it doesn't already exist
                os.makedirs(newFolder)
                print(f"Folder '{newFolder}' created successfully in the Downloads directory.")
            except FileExistsError:
                print(f"Folder '{newFolder}' already exists in the Downloads directory.")
            except Exception as e:
                print(f"An error occurred: {e}")



    def populateFolder(self):
        isFile = False #This boolean keeps track if their are any files located in the downloads directory
        for filename in os.listdir(self.rootDir): #Loops through every item in downloads
            suffix = os.path.splitext(filename)[1]
            if suffix != "": #if the item is a folder, the suffix will be null so this statement makes sure it is a file
                isFile = True
                for key, value in self.folderDictionary.items(): #This loops through the dictionary and checks to see if the said file extension is located in the dictionary
                    if suffix in value:
                        value.remove(suffix) #Value will now only store extensions that were not found
                        source_file = os.path.join(self.rootDir, filename) #These 3 statements create the new directory path for the file in appropriate folder
                        destination_dir = os.path.join(self.rootDir, key) 
                        destination_file = os.path.join(destination_dir, filename)
                        shutil.move(source_file, destination_file) #file is finally moved
                        print(f"Moved: {filename}")
                    if value != []: #This displays the extensions that were not found
                        print(f"file not present with {value} extension")
        if isFile == False:
            print("No files found")



        


    
if __name__ == "__main__":
    BensFolder = Downloads()
    BensFolder.createDictionary()
    BensFolder.createFolder()
    BensFolder.populateFolder()



    