import hashlib
import logging

import shortuuid
from src.controllers.auth_controller import Authentication
from utils.config_class import Config
from db.database_operations import create_table,write_to_database

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level = logging.DEBUG,
                    filename = 'logs.txt')
logger = logging.getLogger('main') 

def create_admin():
    query = 'INSERT INTO authentication (user_id,username,password,role,pwd_changed) VALUES (?,?,?,?,?)'
    password = 'Chetna@12'
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_id = int(shortuuid.ShortUUID('123456789').random(length=4))
    data = (user_id,'chetna',hashed_password,'admin',1)
    write_to_database(query, data)
def start():
    create_table(Config.QUERY_FOR_CREATE_AUTH_TABLE)
    create_table(Config.QUERY_FOR_CREATE_HELPDESK_DETAILS_TABLE)
    create_table(Config.QUERY_FOR_CREATE_BOOKINGS_TABLE)
    create_table(Config.QUERY_FOR_CREATE_ROOMS_DETAILS_TABLE)
    create_admin()
    logger.info(Config.WELCOME_LOGGING_INFO)
    print(Config.WELCOME_MESSAGE)   
    Authentication()  

if __name__ == '__main__':
    start()