import configparser


def getconfig():
    config = configparser.ConfigParser()
    config.read('C://Users//basav//PycharmProjects//ApiIntegration_MIko//Testcases//Base//utilities//properties.ini')
    return config
