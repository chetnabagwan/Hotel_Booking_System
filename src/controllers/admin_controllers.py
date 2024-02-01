import hashlib
import logging
from db.database_operations import write_to_database as add_data,update_data,fetch_data,display_data
from utils.config_class import Config
import sqlite3

logger = logging.getLogger('admin')

class Admin:

    @staticmethod
    def add_rooms(r_type, r_price) :
        add_data(Config.QUERY_TO_ADD_IN_ROOM_DETAILS_TABLE,(r_type, r_price))

    @staticmethod        
    def del_rooms(r_no) :     
        add_data(Config.QUERY_TO_DEL_IN_ROOM_DETAILS_TABLE,(r_no,))
           
    @staticmethod
    def add_receptionists(username,password,emp_email,emp_age,emp_gender,emp_phone):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()    

        try:
            
            add_data([Config.QUERY_TO_ADD_IN_AUTH_TABLE,Config.QUERY_TO_ADD_IN_HELPDESK_DETAILS_TABLE],[(username,hashed_password),(emp_email,emp_age,emp_phone,emp_gender)])

        except sqlite3.Error as e:
            raise e
           
    @staticmethod    
    def del_receptionist(emp_id):   
       try:
         add_data(Config.QUERY_TO_DELETE_FROM_AUTH_TABLE,(emp_id,))
       except sqlite3.Error as e:
           raise e

    @staticmethod
    def update_rooms_info(room_no,r_type,r_price) :
        update_data(Config.QUERY_TO_UPDATE_ROOM_DETAILS,(room_no,r_type,r_price))
        
    @staticmethod 
    def getroom(room_no):
        room_info = fetch_data(Config.QUERY_TO_FETCH_ROOM,room_no)
        return room_info
    
    @staticmethod
    def getrecep(emp_id):
        recep_info = fetch_data(Config.QUERY_TO_FETCH_RECEPTIONIST,emp_id)
        return recep_info

    @staticmethod
    def receptionist_info():
        data = display_data(Config.QUERY_TO_DISPLAY_ALLRECEPTIONIST_DETAILS)
        return data