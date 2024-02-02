import hashlib
import logging
from utils.config_class import Config
from db import database_operations 
import datetime
import sqlite3

logger = logging.getLogger('receptionist')

class Receptionist:

    @staticmethod
    def checkin():
        pass
    
    @staticmethod
    def checkout():
        pass
    
    @staticmethod
    def recep_details(emp_id):
        data = database_operations.display_data(Config.QUERY_TO_DISPLAY_SELFRECEPTIONIST_DETAILS,emp_id)
        return data

    @staticmethod
    def change_default_password(user_id,old_pswd,new_pswd):
        hashed_old_password = hashlib.sha256(old_pswd.encode()).hexdigest() 
        hashed_new_password = hashlib.sha256(new_pswd.encode()).hexdigest() 
        print(hashed_old_password)
        print(hashed_new_password)
        pwd = database_operations.fetch_data(Config.QUERY_TO_FETCH_PASSWORD_FROM_AUTH,user_id)
        try:
            if pwd[0] == hashed_old_password:
                database_operations.update_data(Config.QUERY_TO_CHANGE_DEFAULT_PASSWORD,(hashed_new_password,user_id))
        except sqlite3.Error as e:
            raise e
    
    @staticmethod
    def update_my_details(emp_id,mail,age,phone):  
        try:
            database_operations.update_data(Config.QUERY_TO_UPDATE_EMP_DETAILS,(mail,age,phone,emp_id))
        except sqlite3.Error as e:
            raise e