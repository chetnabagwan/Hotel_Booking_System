import hashlib
from db.database_operations import write_to_database,update_data,fetch_data,display_data
from utils.config_class import Config
import sqlite3
import shortuuid

class Admin:

    @staticmethod
    def add_rooms(r_type, r_price) :
        room_id = int(shortuuid.ShortUUID('123456789').random(length=4))
        write_to_database(Config.QUERY_TO_ADD_IN_ROOM_DETAILS_TABLE,(room_id,r_type, r_price))

    @staticmethod        
    def del_rooms(room_id) :     
        write_to_database(Config.QUERY_TO_DEL_IN_ROOM_DETAILS_TABLE,(room_id,))
           
    @staticmethod
    def add_receptionists(username,password,emp_email,emp_age,emp_gender,emp_phone):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()  
        user_id = int(shortuuid.ShortUUID('123456789').random(length=4))
        try:
            write_to_database([Config.QUERY_TO_ADD_IN_AUTH_TABLE,Config.QUERY_TO_ADD_IN_HELPDESK_DETAILS_TABLE],[(user_id,username,hashed_password),(user_id,emp_email,emp_age,emp_phone,emp_gender)])
        except sqlite3.Error as e:
            raise e
           
    @staticmethod    
    def del_receptionist(user_id):   
       try:
         write_to_database(Config.QUERY_TO_DELETE_FROM_AUTH_TABLE,(user_id,))
       except sqlite3.Error as e:
           raise e

    @staticmethod
    def update_rooms_info(room_id,r_type,r_price) :
        update_data(Config.QUERY_TO_UPDATE_ROOM_DETAILS,(room_id,r_type,r_price))
        
    @staticmethod 
    def getroom(room_id):
        room_info = fetch_data(Config.QUERY_TO_FETCH_ROOM,room_id)
        return room_info
    
    @staticmethod
    def getrecep(emp_id):
        recep_info = fetch_data(Config.QUERY_TO_FETCH_RECEPTIONIST,emp_id)
        return recep_info

    @staticmethod
    def receptionist_info():
        data = display_data(Config.QUERY_TO_DISPLAY_ALLRECEPTIONIST_DETAILS)
        return data
    
    @staticmethod
    def view_all_bookings():
        data = display_data(Config.QUERY_TO_VIEW_ALL_BOOKINGS)
        return data