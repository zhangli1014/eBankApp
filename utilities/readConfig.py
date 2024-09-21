import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('ebank info','baseURL')
        return url

    @staticmethod
    def getUserName():
        username = config.get('ebank info','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('ebank info','password')
        return password