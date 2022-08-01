from re import U

import requests
from pytest_html.extras import url

from Testcases.Base.utilities.configurations import getconfig
from Testcases.Base.utilities.resources import Apiresources


def test_gender():
    url = getconfig()['PROD']['HOST'] + Apiresources.gender
    r = requests.get(url)

    print(r.status_code)
    print(r.text)


def test_Mathparser():
    url = getconfig()['PROD']['HOST'] + Apiresources.math_parser

    res = requests.get(url)
    print(res.status_code)
    print(res.text)
    assert res.status_code == 200


def test_Mathtable():
    url = getconfig()['PROD']['HOST'] + Apiresources.Mathtable

    re = requests.get(url)
    re.status_code
    print(re.status_code)
    assert re.status_code == 200
    print(re.text)


def test_whendidsomethinghappen():
    url = getconfig()['PROD']['HOST'] + Apiresources.whendsH
    re1 = requests.get(url)
    print(re1.text)
    assert re1.status_code == 200


def test_mainconversion():
    url = url = getconfig()['PROD']['HOST'] + Apiresources.main_conversion
    mc = requests.get(url)
    print(mc.text)
    print(mc.status_code)
    print(mc.content)
    assert mc.status_code == 200


def test_Maths():
    url = url = getconfig()['PROD']['HOST'] + Apiresources.maths
    m = requests.get(url)
    print(m.status_code)
    print(m.text)
    assert m.status_code == 200


def test_translate():
    url = url = getconfig()['PROD']['HOST'] + Apiresources.translate_resource
    t = requests.get(url)
    print(t.status_code)
    print(t.text)
    print(t.content)


'''def test_distance():
    url = getconfig()['PROD']['HOST'] + Apiresources.distance
 files = {'file': open('C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//Base//utilities//data'
                          '//distance.txt', 'rb')}'''


#  d = requests.get(url)
#  print(d.status_code)
#  print(d.text)
#  assert d.status_code == 200


def test_Weather():
    url = getconfig()['PROD']['HOST'] + Apiresources.weather
    files = {'file': open('C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//Base//utilities//data'
                          '//weather.txt', 'rb')}
    W = requests.get(url, files=files)
    print(W.text)
    print(W.status_code)
    print(W.content)
    assert W.status_code == 200


'''def test_unit():
   files = {'file': open('C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//Base//utilities//data'
                          '//unit.txt', 'rb')}
  
   U = requests.get(url, files=files)
   url = getconfig()['PROD']['HOST'] + Apiresources.unit
      print(U.text)
    print(U.status_code)
    print(U.content)'''

'''def test_mass():
    url = getconfig()['PROD']['HOST'] + Apiresources.Mass
    files = {'file': open(
        'C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//Base//utilities//data//mass.txt', 'rb')}
    m = requests.get(url, files=files)
    print(m.content)
    print(m.text)
    assert m.status_code == 200
    print(m.headers)'''


def test_noun():
    url = getconfig()['PROD']['HOST'] + Apiresources.noun
    n = requests.get(url)
    print(n.text)
    print(n.status_code)
    print(n.content)
    assert n.status_code == 200


def test_time():
    url = getconfig()['PROD']['HOST'] + Apiresources.time
    t = requests.get(url)
    t.status_code
    print(t.status_code)
    print(t.text)
    print(t.content)


def test_time_numeric():
    url = getconfig()['PROD']['HOST'] + Apiresources.Time_numeric
    T = requests.get(url)
    print(T.text)
    print(T.status_code)
    assert T.status_code == 200


def test_temperature():
    url = getconfig()['PROD']['HOST'] + Apiresources.temperature
    temp = requests.get(url)
    print(temp.status_code)
    print(temp.text)
    assert temp.status_code == 200


def test_unit():
    url = getconfig()['PROD']['HOST'] + Apiresources.unit
    d = requests.get(url)
    print(d.status_code)
    print(d.text)
    assert d.status_code == 200


def test_mass1():
    url = getconfig()['PROD']['HOST'] + Apiresources.Mass
    A = requests.get(url)
    print(A.text)
    print(A.status_code)
    print(A.content)
    print(A.headers)


def test_Massnumeric():
    url = getconfig()['PROD']['HOST'] + Apiresources.MassNumeric
    mn = requests.get(url)
    print(mn.text)
    print(mn.status_code)
    assert mn.status_code == 200


def test_volume():
    url = getconfig()['PROD']['HOST'] + Apiresources.volume
    v = requests.get(url)
    print(v.status_code)
    print(v.content)
    print(v.text)
    print(v.headers)


def test_volume_numeric():
    url = getconfig()['PROD']['HOST'] + Apiresources.volume_numeric
    vn = requests.get(url)
    print(vn.text)
    print(vn.status_code)
    print(vn.headers)
    assert vn.status_code == 200


def test_area():
    url = getconfig()['PROD']['HOST'] + Apiresources.Area
    Aa = requests.get(url)
    print(Aa.status_code)
    print(Aa.text)
    print(Aa.content)


def test_mass2():
    url = url = getconfig()['PROD']['HOST'] + Apiresources.Mass2
    m2 = requests.get(url)
    print(m2.text)
    print(m2.status_code)
    print(m2.content)


def test_angle():
    url = url = getconfig()['PROD']['HOST'] + Apiresources.Angle
    e = requests.get(url)
    print(e.status_code)
    print(e.text)
    print(e.content)
    assert e.status_code == 200


def test_digital_storage():
    url = getconfig()['PROD']['HOST'] + Apiresources.digital_storage
    d = requests.get(url)
    print(d.text)
    print(d.status_code)
    print(d.content)
    assert d.status_code == 200


def test_digital_storage_numeric():
    url = getconfig()['PROD']['HOST'] + Apiresources.digital_storage_numeric
    dn = requests.get(url)
    print(dn.status_code)
    print(dn.text)
    print(dn.content)


def test_distance2():
    url = getconfig()['PROD']['HOST'] + Apiresources.distance
    d2 = requests.get(url)
    print(d2.status_code)
    print(d2.text)
    print(d2.content)
