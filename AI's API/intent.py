import json

import requests
from coverage import data


def test_intent():
    url = " http://35.212.138.183:8000/mikoNLPIntentServiceAndEntityDetection"
    files = {'file': open("/Testcases/AI's API/IntentEntityDetection.json", 'rb')}
    json_payload=json.loads(files)

    i = requests.post(url,json=json_payload)
    print(i.status_code)
    print(i.content)
    json_o=i.text
    json_out=json.loads(json_o)
    print(json_out)

