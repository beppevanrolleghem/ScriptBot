import sys
import json
cast=[]
Scenes = '"Scenes":{'

def CheckScene(sceneString):
    Data = '"lines":[{'
    linesEtc=sceneString = sceneString
    while(True):
        if (linesEtc.find("<p>") == -1 or linesEtc.find(":") == -1 or linesEtc.find("</p>") == -1):
            print("NO TAGS FOUND TO CREATE A LINE, MOVING ON TO THE NEXT ONE")
            break
        temp = linesEtc[linesEtc.find("<p>"):]
        temp = temp[:temp.find("</p>")]
        noBtag = temp.replace("<b>", "")
        noBtag = noBtag.replace("</b>", "")
        noBtag = noBtag[noBtag.find("<p>")+3:noBtag.find("</p>")]
        character = noBtag[:noBtag.find(":")]
        if not(character in cast):
            cast.append(character)
        line = noBtag[noBtag.find(":")+2:]
        line = line.replace('"', '\\"')
        if (len(character) == 0) or len(line) == 0:
                    print("NO CHARACTER FOUND OR NO LINE FOUND,\n LINE = " + line + "\n BY = " + character)
                    break
        Data = Data+'"Character":"'+character+'","Line":"'+line+'"},{'
        linesEtc=linesEtc[len(noBtag):]
    Data=Data[:len(Data)-2]+"]"
    return Data


file = sys.argv[1]
with open(file, "r") as infile:
        script=infile.read().replace('\n', '\\n')
SceneCounter = 1
while (True):
    if(script.find("[Scene:") == -1):
        break
    TestFromSceneOn = script[script.find("[Scene:")+7:]
    tempEndOfScript= TestFromSceneOn[:TestFromSceneOn.find("[Scene:")]
    Desc = tempEndOfScript[:tempEndOfScript.find("]")]
    ToConvLines=tempEndOfScript[tempEndOfScript.find("]"):]
    Lines = CheckScene(ToConvLines)
    Scenes = Scenes+'"'+str(SceneCounter)+'":{"SceneDescription":"'+Desc+'"},'+Lines+"},"
    script = TestFromSceneOn[TestFromSceneOn.find("[Scene:")+7:]
    SceneCounter = SceneCounter+1
Scenes = Scenes[:len(Scenes)-1]+"}"
castStr='"'
for member in cast:
    if(len(member) > 25):
        continue
    castStr=castStr+member+'","'
castStr = castStr[:len(castStr)-2]+']'
with open(file+".json", "w+") as outfile:
    outfile.write('{"Episode":{"Cast":['+castStr+','+Scenes+'}')

#print(TestFromSceneOn)
