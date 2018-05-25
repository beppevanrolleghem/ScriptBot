import sys
import json
cast=[]
Scenes = '"Scenes":{\n\t\t"0":{"SceneDescription":"NONE","lines":[]},'
if len(sys.argv) > 2:
    title=sys.argv[2]
else:
    title="1"

def CheckScene(sceneString):
    Data = '\t\t\t"lines":[{"Character":"","Line":""},'
    linesEtc=sceneString
    while(True):
        if (linesEtc.find("<p>") == -1 or linesEtc.find(":") == -1 or linesEtc.find("</p>") == -1):
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
        if (len(character) == 0) or len(line) == 0:
                    break
        Data = Data+'\n\t\t\t\t{"Character":"'+character+'","Line":"'+line+'"},'
        linesEtc=linesEtc[len(noBtag):]
    Data=Data[:len(Data)-1]+"]\n\t\t\t"
    return Data


file = sys.argv[1]
with open(file, "r") as infile:
        script=infile.read().replace('"', '').replace('\\', 'BACKSLASH').replace('\n','NEWLINE').replace('\t', 'TAB')
SceneCounter = 1
while (True):
    if(script.find("[Scene:") == -1):
        break
    TestFromSceneOn = script[script.find("[Scene:")+7:]
    tempEndOfScript= TestFromSceneOn[:TestFromSceneOn.find("[Scene:")]
    Desc = tempEndOfScript[:tempEndOfScript.find("]")]
    ToConvLines=tempEndOfScript[tempEndOfScript.find("]"):]
    Lines = CheckScene(ToConvLines)
    Scenes = Scenes+'\n\t\t"'+str(SceneCounter)+'":{\n\t\t\t"SceneDescription":"'+Desc+'",\n'+Lines+"},"
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
    outfile.write('{"Content":{\n\t"Cast":['+castStr+',\n\t'+Scenes[:len(Scenes)-1]+'\n\t\t}\n\t},\n\t"Title":"'+file+'"}\n')

#print(TestFromSceneOn)
