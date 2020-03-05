import os
import random
import glob


TypeP = {"WARNING": "\033[1;33;40m", "INFO": "\033[1;35;40m", "ERROR": "\033[1;31;40m", "GOOD": "\033[1;32;40m", "INPUT": "\033[1;34;40m" }

def displayout(typep, message):
    print(typep + "[IDE]: " + message + "\033[0;37;40m")

def inputout(typep, message):
    return input(typep + "[IDE]: " + message + "\033[0;37;40m: ")

#look for the programming dir
try:
    files = os.listdir('/programming/')
    for i in files:
        displayout(TypeP["GOOD"], i) #list all projects in the dir
except IOError:
    os.system("mkdir /programming/") # make a dir if no programming folder is found


EditingProject = inputout(TypeP["INPUT"], "Enter a project name to edit: ") # find a name to edit

os.chdir("/programming/") # change the working dir to the programming dir

FileTrue = (os.path.exists("/programming/" + EditingProject)) # finds if the project file exists



if not FileTrue: # checks if the file is a thing
    displayout(TypeP["WARNING"], "File not accessible")
    
    while True:
        Choice = inputout(TypeP["INPUT"], "Would you like to make a new project? [y]es [n]o: ")
        
        if Choice == 'y' or Choice == 'yes':
            os.system("mkdir " + EditingProject) # make a project
            break

        elif Choice == 'n' or Choice == 'no':
            exit() # exit the ide

        else:
            displayout(TypeP["ERROR"], "Make Sure you enter only what is above...") # the user did not enter what we have

os.chdir("/programming/" + EditingProject + "/") # change the dir to the programming dir

WorkingF = "main.cpp" # set the defalt file to edit


while True:
    AllCpp = []
    AllH = []
    AllTxt = []

    # find all files in the working dir
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".cpp"):
                AllCpp.append(file)
            elif file.endswith(".h"):
                AllH.append(file)
            elif file.endswith(".o"):
                os.system("rm " + file)
            else:
                AllTxt.append(file)
            

    addString = ""
    addStringH = ""
    addStringTxt = ""

    # convert them to a string
    for i in AllCpp:
        addString += i + " "
    for i in AllH:
        addStringH += i + " "
    for i in AllTxt:
        addStringTxt += i + " "


    while True:
        # show the options
        keepEditing = inputout(TypeP["INPUT"], "[Enter] continue, [y] continue, [n] exit, [edit/new] create or edit, [list] list files, [c] compile code: ")

        if keepEditing == '' or keepEditing == 'y':
            #start editing the file
            break

        elif keepEditing == 'n':
            #exit ide
            exit()

        elif keepEditing == 'new' or keepEditing == 'edit' or keepEditing == 'n' or keepEditing == 'e':
            # Make or edit files
            WorkingF = inputout(TypeP["INPUT"], "Enter the file name:  ")
            break

        elif keepEditing == 'list' or keepEditing == 'l':
            # list all files
            displayout(TypeP["GOOD"], "CPP: " + addString)
            displayout(TypeP["GOOD"], "H: " + addStringH)
            displayout(TypeP["GOOD"], "OTHER: " + addStringTxt)

        elif keepEditing == 'c':
            # compile and run
            displayout(TypeP["WARNING"], "Compiling...")
            os.system("g++ -Wall -O2 -o main_Compiled.o " + addString)
            displayout(TypeP["GOOD"], "RUNNING")
            os.system("./main_Compiled.o")
            displayout(TypeP["GOOD"], "Done!")

            
        else:
            displayout(TypeP["ERROR"], "Please enter only what is above...") # the user did not enter what we had


    os.system("vim " + WorkingF) # edit the file



    


