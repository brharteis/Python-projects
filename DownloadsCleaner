import os
import shutil
from pathlib import Path


class Downloads:

    rootDir = str(Path.home()) + "/Downloads"


    def __init__(self):
        self.fileList = []
        self.extensionList = []



    def listFileTypes(self):
        extensions = set()
        for file in os.listdir(self.rootDir):
            extension = os.path.splitext(file)
            #extension becomes a tuple containing the file name and the extension
            
            if extension[1]:  # Ensure the extension is not empty
                extensions.add(extension[1])

        if extensions:
            print(*extensions, sep=", ") 
        


    def createDictionary(self):
        folderDictionary = {}  
        folderName = input("Enter the name of a folder: ") #Loops over however many folders the user chooses
        folderDictionary[folderName] = []
        while folderName != "q":
            fileType = input("Enter the file type you would like to store in this folder: ")
            while fileType != "q":
                self.extensionList.append(fileType)
                folderDictionary[folderName].append(fileType) #This statement adds a file type to the list of an already existing folder
                fileType = input("Enter the file type you would like to store in this folder (q to quit): ") #These next few lines of code do the same thing as previous lines but allows the user to quit
                if fileType != "q":
                    self.extensionList.append(fileType)
                    folderDictionary[folderName].append(fileType)
                    fileType = input("Enter the file type you would like to store in this folder (q to quit): ")
                    

                self.fileList = [] #This statement empties the list for the next folder
                

            
            folderName = input("Enter the name of a folder (q to quit): ")
            if folderName not in folderDictionary and folderName != "q":
                folderDictionary[folderName] = []


        return folderDictionary
            
        

    
    def createFolder(self, folderDictionary):
        for key in folderDictionary: #Loops through all folders given by user
            newFolder = os.path.join(self.rootDir, key) #Creates a directory path for folder
            try: #This will add the folder if it doesn't already exist
                os.makedirs(newFolder)
                print(f"Folder '{newFolder}' created successfully in the Downloads directory.")
            except FileExistsError:
                print(f"Folder '{newFolder}' already exists in the Downloads directory.")
            except Exception as e:
                print(f"An error occurred: {e}")



    def populateFolder(self, dict):
        movedExt = []
        isFile = False #This boolean keeps track if their are any files located in the downloads directory
        for filename in os.listdir(self.rootDir): #Loops through every item in downloads
            suffix = os.path.splitext(filename)[1]
            if suffix != "": #if the item is a folder, the suffix will be null so this statement makes sure it is a file
                isFile = True
                for key, value in dict.items(): #This loops through the dictionary and checks to see if the said file extension is located in the dictionary
                    if suffix in value:
                        source_file = os.path.join(self.rootDir, filename) #These 3 statements create the new directory path for the file in appropriate folder
                        destination_dir = os.path.join(self.rootDir, key) 
                        destination_file = os.path.join(destination_dir, filename)
                        shutil.move(source_file, destination_file) #file is finally moved
                        print(f"Moved: {filename}")
                        movedExt.append(suffix)

               
        if isFile == False:
            print("No files found")

        else:
            difference = [item for item in self.extensionList if item not in movedExt]
            if difference:
                print(f"Extension(s) {", ".join(map(str, difference))} were not found")


    def autoSort(self): #autoSort checks every folder in the downloads dir and stores the extensions being stored in that folder and 
        #chekcs files in download dir to see if they belong to any existing folder and moves them
        extensionTypes = {} #Dict that uses existing folders as keys and list of extensions located in folder as values
        extSet = set() #Set stores extensions
        
        
        for item in os.listdir(self.rootDir): #Loops through every item in downloads
            extensionTypes[item] = set() 
            item_path = os.path.join(self.rootDir, item)
            if os.path.isdir(item_path): #checks to see if item is a folder
                for file in os.listdir(item_path): #Loops through every file located in folder
                    suffix = os.path.splitext(file)[1]
                    if suffix != "":
                        extensionTypes[item].add(suffix) #adds extension to set for every item in folder


       
        #print(extensionTypes)
        self.populateFolder(extensionTypes)




        



        


    
if __name__ == "__main__":
    BensFolder = Downloads()
    folderDict = BensFolder.createDictionary()
    BensFolder.createFolder(folderDict)
    BensFolder.populateFolder(folderDict)
    BensFolder.autoSort()



    
