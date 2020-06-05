import os, csv
from os.path import isfile, join
'''
From Chosen parent directory, this crawls through folders looking for tiff folders not in a drawing folder
and puts their location in a csv file.
'''



class Directory_Folder:

    def __init__(self, path, files = []):
        self.name = os.path.split(path)[-1]
        self.path = path
        if not files:
            self.fileContents = [f for f in os.listdir(path) if isfile(join(path, f))]
        else:
            self.fileContents = files


    def path_as_List(self):
            '''splits a path into each piece that corresponds to a mount point, directory name, or file'''
            path = self.path
            allparts = []
            while 1:
                parts = os.path.split(path)
                if parts[0] == path:  # sentinel for absolute paths
                    allparts.insert(0, parts[0])
                    break
                elif parts[1] == path: # sentinel for relative paths
                    allparts.insert(0, parts[1])
                    break
                else:
                    path = parts[0]
                    allparts.insert(0, parts[1])
            return allparts

dir  = input("Enter filepath to record server parent directory: ")
if dir == "test":
    dir = "S:\Project Folders\Aaron Dankert\TEST FILES"
'''
recipientDir = input("Enter filepath to record server parent directory: ")
if recipientDir == "t":
    recipeintDir = ""
'''
log = {"original TIFF folder locations":[]}

for root, dirs, files in os.walk(dir):

    withinDrawings = False
    i = 0
    thisDirectory = Directory_Folder(root, files)
    for folder in thisDirectory.path_as_List():
        if "F5" in folder or "F - " in folder:
            withinDrawings = True
    for folder in thisDirectory.path_as_List():
        ### strip spaces from last directory in path and check if its a tiff folder and whether its in a drawings folder
        if thisDirectory.path_as_List()[-1].strip() in ["TIFF", "Tiff", "tiff", "TIFF"] and not withinDrawings:
                import pdb; pdb.set_trace()
                #root2 = u"\\\\?\\" + root    ### useful for if the filenames are too long
                newFolderRoot = root[:-2]


                alreadyProcessed = False
                for path in log["original TIFF folder locations"]:
                    if path[0] == root:
                        alreadyProcessed = True
                        break

                if not alreadyRecorded:
                    log["original TIFF folder locations"].append([root])
