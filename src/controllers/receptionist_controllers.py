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
            return g_id
        except sqlite3.Error as e:
            raise e
    
    @staticmethod
    def checkout(g_id):
        try:
            room = database_operations.fetch_data(Config.QUERY_TO_GET_ROOMID_FROM_GUESTID,g_id)
            room_id = room[0]
            # database_operations.write_to_database([Config.QUERY_FOR_CHECKOUT,Config.QUERY_TO_CHANGE_ROOM_STATUS],[(g_id,),(room_id,)])
            database_operations.write_to_database(Config.QUERY_FOR_CHECKOUT,(g_id,))
            database_operations.write_to_database(Config.QUERY_TO_CHANGE_ROOM_STATUS,(room_id,))
        except sqlite3.Error as e:
            raise e
    
    @staticmethod
    def view_available_rooms():
        try:
            data = database_operations.display_data(Config.QUERY_TO_FETCH_ALL_AVAILABLE_ROOMS)
            data = [
                {
                    "room_id" : row[0],
                    "room_type" : row[1],
                    "room_price": row[2],
                    "room_status": row[3]
                }
                for row in data
            ]
            return data
        except sqlite3.Error as e:
            raise e

    @staticmethod
    def recep_details(emp_id):
        try:
            data = database_operations.display_data(Config.QUERY_TO_DISPLAY_SELFRECEPTIONIST_DETAILS,emp_id)
            data = [
                {
                    "user_id":row[0],
                    "email":row[1],
                    "age":row[2],
                    "phone-number":row[3],
                    "gender":row[4]
                }
                for row in data
            ]
            return data
        except sqlite3.Error as e:
            raise e

    @staticmethod
    def change_default_password(user_id,old_pswd,new_pswd):
        hashed_old_password = hashlib.sha256(old_pswd.encode()).hexdigest() 
        hashed_new_password = hashlib.sha256(new_pswd.encode()).hexdigest()
        pwd = database_operations.fetch_data(Config.QUERY_TO_FETCH_PASSWORD_FROM_AUTH,user_id)
        try:
            if pwd[0] == hashed_old_password:
                database_operations.update_data(Config.QUERY_TO_CHANGE_DEFAULT_PASSWORD,(hashed_new_password,user_id))
        except sqlite3.Error as e:
            print(e)
    
    @staticmethod
    def update_my_details(emp_id,mail,age,phone):  
        try:
            database_operations.update_data(Config.QUERY_TO_UPDATE_EMP_DETAILS,(mail,age,phone,emp_id))
        except sqlite3.Error as e:
            raise e