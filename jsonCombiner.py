import sys, os

folder = sys.argv[1]
strDataStruct = '{"Episodes":['
for file in os.listdir(folder):
    print(file)
    if(file.endswith('.json')):
        with open(folder+"/"+file, "r") as infile:
            strDataStruct=strDataStruct+infile.read()+","
strDataStruct=strDataStruct[:len(strDataStruct)-1]+"]}"
with open("OUTPUTFILE.json", "w+") as outfile:
    outfile.write(strDataStruct)
