import hashlib
import logging
from utils.config_class import Config
from db import database_operations 
import datetime
import sqlite3

logger = logging.getLogger('receptionist')

class Receptionist:

    # def __init__(self,userid):
    #     self.userid = userid
    #     logging.info(Config.LOGGED_IN)

    # def menu_receptionist(self):
    #     user_input = input(Config.RECEPTIONIST_PROMPT)
    #     while user_input != '6':
    #         match user_input:
    #             case '1':
    #                 pass #checkin()
    #             case '2':
    #                 pass #checkout()
    #             case '3':
    #                 emp_id = int(input())
    #                 Receptionist.recep_details(emp_id)
    #             case '4':
    #                 emp_id = int(input())
    #                 Receptionist.update_details(emp_id)
    #             case _:
    #                 print(Config.WRONG_INPUT_ENTERED_MESSAGE)
    #         user_input = input(Config.RECEPTIONIST_PROMPT)

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
    def change_default_password(username,old_pswd,new_pswd):
        hashed_old_password = hashlib.sha256(old_pswd.encode()).hexdigest() 
        hashed_new_password = hashlib.sha256(new_pswd.encode()).hexdigest() 
        pwd = database_operations.fetch_data(Config.QUERY_TO_FETCH_PASSWORD_FROM_AUTH,username)
        try:
            if pwd[0] == hashed_old_password:
                database_operations.update_data(Config.QUERY_TO_CHANGE_DEFAULT_PASSWORD,(hashed_new_password,username))
        except sqlite3.Error as e:
            raise e
    


    @staticmethod
    def update_details(emp_id):  
        pass
        # self.update_input = input(Config.UPDATE_DETAILS_PROMPT)
        # match self.update_input:
        #     case '1':
        #         email_to_update = input("Enter the new mail:- ")
        #         database_operations.update_data(Config.QUERY_TO_UPDATE_EMP_MAIL,(email_to_update,self.userid,))
        #         logging.debug(Config.UPDATED_SUCCESSFULLY)
        #     case '2':
        #         age_to_update = input("Enter the new age:- ")
        #         database_operations.update_data(Config.QUERY_TO_UPDATE_EMP_AGE,(age_to_update,self.userid,))
        #         logging.debug(Config.UPDATED_SUCCESSFULLY)
        #     case '3':
        #         phone_to_update = input("Enter the new phone number:- ")
        #         database_operations.update_data(Config.QUERY_TO_UPDATE_EMP_PHONE,(phone_to_update,self.userid,))
        #         logging.debug(Config.UPDATED_SUCCESSFULLY)
        #     case '4':
        #         gender_to_update = input("Enter the new gender:- ")
        #         database_operations.update_data(Config.QUERY_TO_UPDATE_EMP_GENDER,(gender_to_update,self.userid,))
        #         logging.debug(Config.UPDATED_SUCCESSFULLY)
        #     case _:
        #         print(Config.WRONG_INPUT_ENTERED_MESSAGE)