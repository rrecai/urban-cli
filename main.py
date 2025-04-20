import requests
import sys
import json

def apicall(word: str):
    response=json.loads(requests.get("https://api.urbandictionary.com/v0/define?term="+word).content)["list"]
    i=1
    for meaning in response:
        print(str(i)+". result:")
        i+=1
        print("definiton:",meaning["definition"])
        print("example:",meaning["example"])

if __name__ == "__main__":
    if len(sys.argv) == 2:
        word = sys.argv[1]
        print("word:",word)
        apicall(word)
    elif len(sys.argv) > 2:
        phrase = "%20".join(sys.argv[1:])
        print("phrase:"," ".join(sys.argv[1:]))
        apicall(phrase)
    else:
        x=json.loads(requests.get("https://api.urbandictionary.com/v0/random").content)
        for entry in x["list"]:
            print(f"word: {entry['word']}")
            print(f"meaning: {entry['definition']}")
            print(f"example: {entry['example']}")
            print("-" * 30)
