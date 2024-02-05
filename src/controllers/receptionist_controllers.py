import hashlib
import shortuuid
from utils.config_class import Config
from db import database_operations 
from datetime import datetime
import sqlite3

class Receptionist:

    @staticmethod
    def checkin(g_name,g_email,g_phone,g_adrs,room_id,check_out_date):
        check_in_date = datetime.now()
        g_id = int(shortuuid.ShortUUID('123456789').random(length=4))
        try:
            database_operations.write_to_database([Config.QUERY_FOR_CHECKIN,Config.QUERY_TO_CHANGE_ROOM_STATUS],
                                                  [(g_id,g_name,g_email,g_phone,g_adrs,room_id,check_in_date,check_out_date),(room_id,)])
        except sqlite3.Error as e:
            raise e
    
    @staticmethod
    def checkout(g_id):
        try:
            room_id = database_operations.fetch_data(Config.QUERY_TO_GET_ROOMID_FROM_GUESTID,g_id)
            # database_operations.write_to_database([Config.QUERY_FOR_CHECKOUT,Config.QUERY_TO_CHANGE_ROOM_STATUS],[(g_id,),(room_id,)])
            database_operations.write_to_database(Config.QUERY_FOR_CHECKOUT,(g_id,))
            database_operations.write_to_database(Config.QUERY_TO_CHANGE_ROOM_STATUS,(room_id,))
        except sqlite3.Error as e:
            raise e
    
    @staticmethod
    def view_available_rooms():
        try:
            data = database_operations.display_data(Config.QUERY_TO_FETCH_ALL_AVAILABLE_ROOMS)
            return data
        except sqlite3.Error as e:
            raise e

    @staticmethod
    def recep_details(emp_id):
        try:
            data = database_operations.display_data(Config.QUERY_TO_DISPLAY_SELFRECEPTIONIST_DETAILS,emp_id)
            return data
        except sqlite3.Error as e:
            raise e

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