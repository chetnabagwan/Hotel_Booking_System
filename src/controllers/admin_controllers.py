import hashlib
import logging
from pwinput import pwinput
from db import database_operations
from utils.config_class import Config
from utils.input_validation import InputValidations

logger = logging.getLogger('admin')

class Admin:
    def __init__(self):  
        print(Config.WELCOME_ADMIN_MESSAGE)

    def menu_admin(self):
        user_input = input(Config.ADMIN_PROMPT)
        while user_input != '8':
            match user_input:
                case '1':
                    r_type=input("Enter room type: ")
                    r_price=input("Enter room price: ")
                    Admin.add_rooms(r_type,r_price)
                case '2':
                    r_no=input("Enter room no : ")
                    Admin.del_rooms(r_no)
                case '3':
                    username = input(Config.PRINT_USERNAME)
                    password = pwinput(prompt=Config.PRINT_PASSWORD)
                    emp_mail = input(Config.ENTER_MAIL)
                    emp_age = int(input(Config.ENTER_AGE))
                    emp_phone = int(input(Config.ENTER_PHONE_NO))
                    emp_gender = input(Config.ENTER_GENDER)
                    Admin.add_receptionists(username,password,emp_mail,emp_age,emp_gender,emp_phone)
                case '4':
                    emp_id= input(Config.ENTER_EMP_ID)
                    Admin.del_receptionist(emp_id)
                case '5':
                    room_no=input("Enter room no to update details : ")
                    r_type = input("Room type : ")
                    r_price = input("Room price : ")
                    Admin.update_rooms_info(room_no,r_type,r_price)
                case '6':
                    database_operations.display_data(Config.QUERY_TO_DISPLAY_ALLRECEPTIONIST_DETAILS)
                case '7':
                    database_operations.display_data(Config.QUERY_TO_DISPLAY_HOTEL_STATUS,Config.LIST_TO_DISPLAY_HOTEL_STATUS)
                case _:
                    print(Config.WRONG_INPUT_ENTERED_MESSAGE)
        user_input = input(Config.ADMIN_PROMPT)

    @staticmethod
    def add_rooms(r_type,r_price) :
        database_operations.add_data(Config.QUERY_TO_ADD_IN_ROOM_DETAILS_TABLE,(r_type,r_price))

    @staticmethod        
    def del_rooms(r_no) :     
        database_operations.delete_data(Config.QUERY_TO_DEL_IN_ROOM_DETAILS_TABLE,r_no)
           
    @staticmethod
    def add_receptionists(username,password,emp_email,emp_age,emp_gender,emp_phone):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()     
        database_operations.add_data(Config.QUERY_TO_ADD_IN_AUTH_TABLE,(username,hashed_password))
        database_operations.add_data(Config.QUERY_TO_ADD_IN_HELPDESK_DETAILS_TABLE,(emp_email,emp_age,emp_phone,emp_gender))

    @staticmethod    
    def del_receptionist(emp_id):   
        database_operations.delete_data(Config.QUERY_TO_DELETE_FROM_AUTH_TABLE,emp_id)
        database_operations.delete_data(Config.QUERY_TO_DEL_RECEPTIONIST,emp_id)


    @staticmethod
    def update_rooms_info(room_no,r_type,r_price) :
        database_operations.update_data(Config.QUERY_TO_UPDATE_ROOM_DETAILS,room_no,r_type,r_price)
        
    @staticmethod 
    def getroom(room_no):
        room_info = database_operations.fetch_data(Config.QUERY_TO_FETCH_ROOM,room_no)
        return room_info
    
    @staticmethod
    def getrecep(emp_id):
        recep_info = database_operations.fetch_data(Config.QUERY_TO_FETCH_RECEPTIONIST,emp_id)
        return recep_info

    @staticmethod
    def receptionist_info():
        data = database_operations.display_data(Config.QUERY_TO_DISPLAY_ALLRECEPTIONIST_DETAILS)
        return data