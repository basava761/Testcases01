import json

import requests
import requests as requests


def test_intent():
    url = " http://35.212.138.183:8000/mikoNLPIntentServiceAndEntityDetection"
    file = open(
        "C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//AI's API//IntentEntityDetection.json", )
    json_input = file.read()
    json_input1 = json.loads(json_input)
    print(json_input1)
    res = requests.post(url, json=json_input1)
    print(res.text)
    print(res.status_code)
    print(res.content)
    assert res.status_code == 200


def test_EntityDetection():
    url = " http://35.212.138.183:8003/ner"
    files = open(
        "C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//AI's API//IntentEntityDetection.json")

    json_input2 = files.read()
    json_data = json.loads(json_input2)
    res1 = requests.post(url, json=json_data)
    print(res1.status_code)
    print(res1.text)
    print(res1.content)


def test_PersonRecommendation():
    url = "http://35.212.138.183:8049/get_rec"
    file = open("C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//AI's API//recomm.json")
    json_i = file.read()
    json_d = json.loads(json_i)
    p = requests.get(url, json=json_d)
    print(p.text)
    print(p.status_code)
    assert p.status_code == 200


def test_Profanity():
    url = "http://35.212.138.183:5000/detect_multiple_lang"
    file = open("C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//AI's API//profanity.txt")
    json_in = file.read()
    jsondata = json.loads(json_in)
    f = requests.post(url, json=jsondata)
    print(f.status_code)
    print(f.text)
    print(f.content)


def test_EntityFinder():
    url = "http://35.212.138.183:5008/entity_finder"
    file = open("C://Users//basav//PycharmProjects\ApiIntegration_MIko//Testcases//AI's "
                "API//.pytest_cache//entityfinder.json")
    json_e = file.read()
    json_1d = json.loads(json_e)
    e = requests.post(url, json=json_e)
    print(e.status_code)
    print(e.text)
    assert e.status_code == 200


def test_sentensereco():
    url = "http://35.212.138.183:8049/get_rec"
    file = open("C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//AI's API//senreco.txt")
    f_i = file.read()
    input = json.loads(f_i)
    s = requests.get(url, json=input)
    print(s.status_code)
    print(s.text)
    print(s.content)
    assert s.status_code == 200
