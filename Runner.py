import sys, os

folder = sys.argv[1]
x = 0
for file in os.listdir(folder):
    x = x+1
    print(file)
    if(file.endswith('.html')):
        os.system('python FriendsConverter.py "'  + folder+"/"+file+'" '+str(x))

os.system('python jsonCombiner.py "'+folder+'"')
