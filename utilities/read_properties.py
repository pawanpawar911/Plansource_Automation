#it requires the configparser

import configparser

config = configparser.RawConfigParser()  # there is class rawConfigparser in config parser to parse the data

config.read(".\\configuration\\config.ini")

class ReadConfig:
    @staticmethod 
    def getWebURL():
        url = config.get('common info', 'base_url')
        return url
         
    @staticmethod  
    def get_valid_usrName():
        valid_username = config.get('common info', 'valid_usrName')
        return valid_username
         
    @staticmethod
    def get_valid_passWord():
        valid_password = config.get('common info', 'valid_passWord')
        return valid_password
        
    @staticmethod
    def get_invalid_usrName():
        invalid_username = config.get('common info', 'invalid_usrName')
        return invalid_username
        
    @staticmethod
    def get_invalid_passWord():
        invalid_password = config.get('common info', 'invalid_passWord')
        return invalid_password
    
    @staticmethod
    def get_api_url():
        api_url = config.get('common info', 'api_url')
        return api_url
    
    @staticmethod
    def get_referer():
        referer = config.get('common info', 'referer')
        return referer
    
    @staticmethod
    def get_session_id():
        session_id = config.get('common info', 'session_id_value')
        return session_id
        