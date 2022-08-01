import requests
import json


def test_mikoservletpoc():
    url = 'http://miko3-aks-agic.miko2.co.in/mikoservletpoc/miko-servlet-poc/recommendation2'
    files = {'file': open('C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//test_miko-servlet-poc'
                          '//servalet-poc data//withoutslot.txt', 'rb')}

    m = requests.get(url, files=files,)
    print(m.status_code)
    print(m.text)
    assert m.status_code == 200
