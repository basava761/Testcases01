import requests
import json


def test_launch():
    url = 'http://miko3-aks-agic.miko2.co.in/mikoclassroom/classroom/classroom'
    file = open(
        "C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//test_classroom Api's// LaunchRequest .txt")
    inp = file.read()
    inp_req = json.loads(inp)
    l = requests.post(url, json=inp_req)
    print(l.text)
    print(l.status_code)


def test_DElementSelected():
    url = "http://miko3-aks-agic.miko2.co.in/mikoclassroom/classroom/classroom"
    file = open(
        "C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//test_classroom Api's//displayelement "
        "selected.txt")
    input = file.read()
    json_input = json.loads(input)

    d = requests.post(url, json=json_input)
    print(d.status_code)
    print(d.text)
    print(d.content)
    assert d.status_code == 200


def test_intentRequest():
    url = "http://miko3-aks-agic.miko2.co.in/mikoclassroom/classroom/classroom"
    file = open(
        "D://Miko//OneDrive//Desktop//Automation//Testcases//test_classroom Api's//intent.txt")
    input1 = file.read()
    json_input = json.loads(input1)
    i = requests.post(url, json=json_input)
    print(i.status_code)
    print(i.text)
    print(i.content)
    assert i.status_code == 200


def test_SessionEndedRequest():
    url = "http://miko3-aks-agic.miko2.co.in/mikoclassroom/classroom/classroom"
    file = open("C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//test_classroom "
                "Api's//SessionEndedRequest.txt")
    int = file.read()
    json_in = json.loads(int)
    s = requests.post(url, json=json_in)
    print(s.status_code)
    print(s.text)
    assert s.status_code == 200


def test_Completedgraph():
    url="http://miko3-aks-agic.miko2.co.in/mikoclassroom/classroom/classroom"
    file = open("D://Miko//OneDrive//Desktop//Automation//Testcases//test_classroom Api's//completed graph.txt")
    int1 = file.read()
    json_in1 = json.loads(int1)
    s1 = requests.post(url, json=json_in1)
    print(s1.status_code)
    print(s1.text)
    assert s1.status_code==200
