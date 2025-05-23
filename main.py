import requests
import sys
import json
def apicall(word: str, url: str="https://api.urbandictionary.com/v0/define?term="):
    response=json.loads(requests.get(url+word).content)["list"]
    i=1
    for meaning in response:
        print(str(i)+". result:")
        i+=1
        print("definiton:",meaning["definition"].replace("[","").replace("]",""))
        print("example:",meaning["example"].replace("[","").replace("]",""))
if len(sys.argv) == 2:
    word = sys.argv[1]
    print("word:",word)
    apicall(word)
elif len(sys.argv) > 2:
    phrase = "%20".join(sys.argv[1:])
    print("phrase:"," ".join(sys.argv[1:]))
    apicall(phrase)
else:
    print("random results:")
    apicall("","https://api.urbandictionary.com/v0/random")
