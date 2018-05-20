import json
import sys, os
Cast = {}

string = sys.argv[1]
temp = ""
arrayOfStrings = []
space = " "
for x in range(0, 100):
    arrayOfStrings.append(space)
    space = space+" "



with open(string, "r") as infile:
    fileNaam=infile.read().replace('\n', '     ')
    array=fileNaam.split()
    arrayFromCast = array[array.index("CAST")+1:]
    Cast=arrayFromCast[:arrayFromCast.index("STAR")];




with open('output.json', 'w+') as outfile:
   json.dump(Cast, outfile)
with open('Temp.txt', 'w+') as outfile:
    outfile.write(temp)
    outfile.close()
