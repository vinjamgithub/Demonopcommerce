import configparser

#rawconfigparser is a predefined paackage.
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")
class ReadConfig:
    @staticmethod
    def getapplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getEmail():
        Email = config.get('common info', 'Email')
        return Email

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password
