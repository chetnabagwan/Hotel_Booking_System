import hashlib
import logging
import sqlite3
from pwinput import pwinput
from utils.config_class import Config
from db import database_operations 

from controllers.admin_controllers import Admin
from controllers.receptionist_controllers import Receptionist

logger = logging.getLogger('authentication')

class Authentication:
    
    # def __init__(self):  
        
    #     return_value = self.login()
    #     if return_value == None:
    #         exit()
    #     userid, role = return_value
    #     if role == 'admin':
    #         objAdmin= Admin()
    #         objAdmin.menu_admin()
    #     else:
    #         objRec = Receptionist(userid)
    #         objRec.menu_()  
        
    # def change_default_password(self):
    #     self.default_password = pwinput(prompt=Config.ENTER_DEFAULT_PASSWORD)
    #     login_success = database_operations.fetch_user(Config.QUERY_TO_VERIFY_LOGIN,self.username,self.default_password)
    #     if login_success == None:
    #         return False
    #     self.new_password = pwinput(prompt=Config.ENTER_NEW_PASSWORD)
    #     self.confirm_password = pwinput(prompt=Config.CONFIRM_PASSWORD)
    #     if self.new_password != self.confirm_password:
    #         return False
    #     self.hashed_password = hashlib.sha256(self.new_password.encode()).hexdigest()
    #     database_operations.update_data(Config.QUERY_TO_CHANGE_DEFAULT_PASWORD,(self.hashed_password,self.username))
    
    @staticmethod
    def login(username,password):  
        hashed_password= hashlib.sha256(password.encode()).hexdigest()   
        login_success_data = database_operations.fetch_user(Config.QUERY_TO_VERIFY_LOGIN,username,hashed_password)
        if login_success_data == None:
            raise sqlite3.Error
        else:
            return login_success_data
        
    