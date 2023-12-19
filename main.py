import logging
from authentication.authentication import Authentication
from utils.config_class import Config
from db.database_operations import create_table

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level = logging.DEBUG,
                    filename = 'logs.txt')
logger = logging.getLogger('main') 

@Config.config_loader
def start():
    create_table(Config.QUERY_FOR_CREATE_AUTH_TABLE)
    create_table(Config.QUERY_FOR_CREATE_HELPDESK_DETAILS_TABLE)
    create_table(Config.QUERY_FOR_CREATE_BOOKINGS_TABLE)
    create_table(Config.QUERY_FOR_CREATE_ROOMS_DETAILS_TABLE)
    logger.info(Config.WELCOME_LOGGING_INFO)
    print(Config.WELCOME_MESSAGE)   
    Authentication()  

if __name__ == '__main__':
    start()