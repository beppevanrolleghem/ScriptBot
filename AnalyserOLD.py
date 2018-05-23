import json
import sys, os
import Analyser
import re



### VARIABLES

Cast = [] #an array of cast members
string = "sys.argv[1]" #the location of the current file we want to convert
temp = "" #temp string
spaces = [] #an array of spaces we want to check since some of the formating is lost and newlines are replaced by a bunch of spaces
spacesRev = []
space = " " #a space var that is used to initiate the spaces list
finishstring = "FINISHEDTHESTRINGS" #finished string meant to check for when we run a huge string through a while loop, when it's done splitting everything, the main string will change name to finishedstring


### VAR INITIATERS


## FILS THE SPACES LIST WITH AMOUNTS OF SPACES WE WILL WANT TO SPLIT FROM.
for x in range(0, 100):
    space = space+" "
    spaces.append(space)

for i in reversed(spaces):
    spacesRev.append(i)

### FUNCTIONS

##SPLITTER
#takes two arguments, the string to split and the array to append the part it split. Checks for any amount of spaces longer then 1 space

def splitter(string, array):
    global spacesRev #get all spaces for comparison
    global finishstring #get universally set finishstring
    index = -1
    lowestStart = -1
    for space in spaces:
        m = re.search(space, string)
        if m is not None:
            tempStart = m.start()
            tempEnd =  m.end()
        else:
            index=-1
            continue
        if (tempEnd > index or index == -1) and (tempStart <= lowestStart or lowestStart == -1):
            index = tempStart
            lowestStart = tempEnd
    if index > -1:
        beforeSplit = string[:index]
        afterSplit = string[lowestStart:]
        array.append(beforeSplit)
        return afterSplit
    else:
        array.append(string)
        return finishstring

def Folder(folder):
    global Cast
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            File(folder+"/"+file)

def File(file):
    global Cast
    with open(file, "r") as infile:
        fileNaam=infile.read().replace('\n', '     ')
        fileNaam = fileNaam.replace('\t', '     ')
        x = 0
        while fileNaam != finishstring:
            fileNaam = splitter(fileNaam, Cast)
            if(x < len(fileNaam)) and x is not 0:
                break
            x = len(fileNaam)
            print('only ' + str(x) + " characters left from file " + file + ", rest is being written to Output/" + file + '.json')
    with open('Output/'+file+'.json', 'w+') as outfile:
       json.dump(Cast, outfile)
    if "CAST" in Cast:
        CheckCast = Cast.index("CAST")
        tempAr =Cast[CheckCast:]
        if "STAR TREK: THE NEXT GENERATION" in tempAr:
            endOfCast = tempAr.index("STAR TREK: THE NEXT GENERATION")
        else:
            endOfCast = -1
    else:
        CheckCast = -1
        endOfCast = -1

    if (CheckCast is not -1) and (endOfCast is not -1):
        print(CheckCast)
        print(endOfCast)
        with open('Output/'+file+'-Casts.json', 'w+') as outfile:
            temp = Cast[CheckCast+1:CheckCast+endOfCast]
            print(temp)
            json.dump(temp, outfile)
    Cast = []


def Main():
    if len(sys.argv) > 1:
        if (os.path.isdir(sys.argv[1])):
            print("folder")
            Folder(sys.argv[1])
        if (os.path.isfile(sys.argv[1])):
            print("file")
            File(sys.argv[1])
        else:
            print("Invalid file")
            input()
    else:
        print('no argument')
        input()



Main()
