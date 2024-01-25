import logging
from utils.config_class import Config
from db import database_operations 
import datetime

logger = logging.getLogger('receptionist')

class Receptionist:

    def __init__(self,userid):
        self.userid = userid
        logging.info(Config.LOGGED_IN)

    def menu_receptionist(self):
        user_input = input(Config.RECEPTIONIST_PROMPT)
        while user_input != '6':
            match user_input:
                case '1':
                    pass #checkin()
                case '2':
                    pass #checkout()
                case '3':
                    emp_id = int(input())
                    Receptionist.recep_details(emp_id)
                case '4':
                    emp_id = int(input())
                    Receptionist.update_details(emp_id)
                case _:
                    print(Config.WRONG_INPUT_ENTERED_MESSAGE)
            user_input = input(Config.RECEPTIONIST_PROMPT)

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