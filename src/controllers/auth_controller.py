import hashlib
import logging
import sqlite3
from utils.config_class import Config
from db import database_operations 

logger = logging.getLogger(__name__)

class Authentication:
  
    @staticmethod
    def login(username,password):  
        hashed_password= hashlib.sha256(password.encode()).hexdigest()   
        login_success_data = database_operations.fetch_user(Config.QUERY_TO_VERIFY_LOGIN,username,hashed_password)
        print(login_success_data)
        if login_success_data == None:
            logger.info(f'Login performed with username : {username} failed, Invalid credentials')
            raise sqlite3.Error
        else:
            return login_success_data
        
    