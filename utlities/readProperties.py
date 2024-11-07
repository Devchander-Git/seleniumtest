import configparser
import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"//configuration/config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=config.get('commonInfo','baseURL')
        return url

    @staticmethod
    def getuseremail():
        useremail=config.get('commonInfo','email')
        return useremail

    @staticmethod
    def getpassWord():
        pwd=config.get('commonInfo','password')

