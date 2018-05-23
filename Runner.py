import sys, os

folder = sys.argv[1]
for file in os.listdir(folder):
    print(file)
    if(file.endswith('.html')):
        os.system('FriendsConverter.py "'  + folder+"/"+file+'"')

os.system('jsonCombiner.py "'+folder+'"')
