import hashlib
import logging
from pwinput import pwinput
from db import database_operations
from utils.config_class import Config
from db.queries.queries_config import Config
from utils.input_validation import password_validation

logger = logging.getLogger('admin')

class Admin:
    def __init__(self):  
        print(Config.WELCOME_ADMIN_MESSAGE)

    def menu_admin(self):
        user_input = input(Config.ADMIN_PROMPT)
        while user_input != '8':
            match user_input:
                case '1':
                    Admin.add_rooms()
                case '2':
                    Admin.del_rooms()
                case '3':
                    Admin.add_receptionists()
                case '4':
                    Admin.del_receptionist()
                case '5':
                    Admin.update_rooms_info()
                case '6':
                    database_operations.display_data(Config.QUERY_TO_DISPLAY_ALLRECEPTIONIST_DETAILS,Config.LIST_TO_DISPLAY_ALLRECEPTIONIST_DETAILS)
                case '7':
                    database_operations.display_data(Config.QUERY_TO_DISPLAY_HOTEL_STATUS,Config.LIST_TO_DISPLAY_HOTEL_STATUS)
                case _:
                    print(Config.WRONG_INPUT_ENTERED_MESSAGE)
        user_input = input(Config.ADMIN_PROMPT)

    def add_rooms() :
        r_type=input("Enter room type: ")
        r_price=input("Enter room price: ")
        database_operations.execute(Config.QUERY_TO_ADD_IN_ROOM_DETAILS_TABLE,(r_type,r_price,))
        print(Config.ROOM_ADDED)
            
    def del_rooms() :     
        r_no=input("Enter room no : ")
        database_operations.execute(Config.QUERY_TO_DEL_IN_ROOM_DETAILS_TABLE,(r_no,))
        print(Config.ROOM_DELETED)
           
    @staticmethod
    def add_receptionists() :
        username = input(Config.PRINT_USERNAME)
        while True:
            password = pwinput(prompt=Config.PRINT_PASSWORD)
            if not password_validation(password):
                print(Config.ENTER_STRONG_PASSWORD)
            else:
                break
        hashed_password = hashlib.sha256(password.encode()).hexdigest()     
        role = input(Config.ENTER_ROLE)
        emp_mail = input(Config.ENTER_MAIL)
        emp_age = int(input(Config.ENTER_AGE))
        emp_phone = int(input(Config.ENTER_PHONE_NO))
        emp_gender = input(Config.ENTER_GENDER)
        database_operations.add_data(Config.QUERY_TO_ADD_IN_AUTH_TABLE,(username,hashed_password,role))
        database_operations.add_data(Config.QUERY_TO_ADD_IN_HELPDESK_DETAILS_TABLE,(emp_mail,emp_age,emp_phone,emp_gender))
        logging.info(Config.REGISTERED_SUCCESSFULLY)

    @staticmethod    
    def del_receptionist():   
        emp_id= input(Config.ENTER_EMP_ID)
        database_operations.delete_data(Config.QUERY_TO_DELETE_FROM_AUTH_TABLE,emp_id)
        database_operations.delete_data(Config.QUERY_TO_DEL_RECEPTIONIST,emp_id)
        logging.warning(Config.DELETED_SUCCESSFULLY)
    

    def update_rooms_info() :
        room_no=input("Enter room no to update details : ")
        print(Config.UPDATE_ROOMS_DETAILS_PROMPT)
        ch=input("Enter your choice: ")
        if ch=='1':
            new_type=input("Enter the new room type")
            database_operations.update_data(Config.QUERY_TO_UPDATE_ROOM_TYPE,room_no)
            print(Config.UPDATED_SUCCESSFULLY)
        
        elif ch=='2':
           price=input("Enter the new price: ")
           database_operations.update_data(Config.QUERY_TO_UPDATE_ROOM_TYPE,room_no)
           print(Config.UPDATED_SUCCESSFULLY)
        else:
            pass
            