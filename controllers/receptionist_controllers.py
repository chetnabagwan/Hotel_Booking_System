import logging
from utils.config_class import Config
from db.queries.queries_config import QueriesConfig
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
                    pass #Billing()
                case '4':
                    database_operations.display_data(QueriesConfig.QUERY_TO_DISPLAY_SELFRECEPTIONIST_DETAILS,self.userid,QueriesConfig.QUERY_TO_DISPLAY_SELFRECEPTIONIST_DETAILS)
                case '5':
                    self.update_details()
                case _:
                    print(Config.WRONG_INPUT_ENTERED_MESSAGE)
            user_input = input(Config.RECEPTIONIST_PROMPT)

    def checkin():
        pass

    def checkout():
        pass

    def billing():
        pass

    def update_details(self):
        self.update_input = input(Config.UPDATE_DETAILS_PROMPT)
        match self.update_input:
            case '1':
                email_to_update = input("Enter the new mail:- ")
                database_operations.update_data(QueriesConfig.QUERY_TO_UPDATE_EMP_MAIL,(email_to_update,self.userid,))
                logging.debug(Config.UPDATED_SUCCESSFULLY)
            case '2':
                age_to_update = input("Enter the new age:- ")
                database_operations.update_data(QueriesConfig.QUERY_TO_UPDATE_EMP_AGE,(age_to_update,self.userid,))
                logging.debug(Config.UPDATED_SUCCESSFULLY)
            case '3':
                phone_to_update = input("Enter the new phone number:- ")
                database_operations.update_data(QueriesConfig.QUERY_TO_UPDATE_EMP_PHONE,(phone_to_update,self.userid,))
                logging.debug(Config.UPDATED_SUCCESSFULLY)
            case '4':
                gender_to_update = input("Enter the new gender:- ")
                database_operations.update_data(QueriesConfig.QUERY_TO_UPDATE_EMP_GENDER,(gender_to_update,self.userid,))
                logging.debug(Config.UPDATED_SUCCESSFULLY)
            case _:
                print(Config.WRONG_INPUT_ENTERED_MESSAGE)