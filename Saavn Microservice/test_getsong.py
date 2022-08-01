import requests
import json


def test_getSong():
    url = 'http://miko3-aks-agic.miko2.co.in/saavn/saavn/getSong'
    files = {'file': open('C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//Saavn '
                          'Microservice//saavan requests//getsong.txt', 'rb')}

    # input=file.read()
    # req_input=json.loads(input)
    g = requests.get(url, files=files)
    print(g.text)
    print(g.status_code)
    assert g.status_code==200


def test_BasedOnGenre():
    url = 'http://miko3-aks-agic.miko2.co.in/saavn/saavn/getSongBasedOnGenre'
    files = {'file': open('C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//Saavn '
                          'Microservice//saavan requests//based on genere.txt', 'rb')}
    b=requests.post(url,files=files)
    print(b.text)
    print(b.status_code)
    assert b.status_code==200
