import sys
import json


file = sys.argv[1]
with open(file, "r") as infile:
        script=infile.read().replace('\n', '\\n')
while (True):
    if(script.find("[Scene:") == -1):
        break
    TestFromSceneOn = script[script.find("[Scene:"):]
    tempEndOfScript= script[:script.find("[Scene:")]
    print(tempEndOfScript)
    script = TestFromSceneOn[script.find("[Scene:")+7:]
    print("END OF TEST")
print(TestFromSceneOn)
