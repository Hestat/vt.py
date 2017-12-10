import requests
import sys
import os
import json

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

user_input = raw_input("Enter the path of your file: ")

assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
f = open(user_input,'r+')
print("Preparing to upload file.")

params = {'apikey': 'PUT_YOUR_KEY_HERE'}
files = {'file': (user_input, open(user_input, 'rb'))}
response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
json_response = response.json()
pp_json(json_response)
f.close()
