import logging
from authentication import Authentication
from utils.config_class import Config
from db.queries.queries_config import QueriesConfig

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level = logging.DEBUG,
                    filename = 'logs.txt')
logger = logging.getLogger('main')

def load_config_files():
    Config.load()
    Config.load_print_statements()
    Config.load_logging_statements()
    QueriesConfig.loadAdminQueries()
    QueriesConfig.loadEmployeeQueries() 

if __name__ == '__main__':   
    load_config_files()
    logger.info(Config.WELCOME_LOGGING_INFO)
    print("\n")
    print(Config.WELCOME_MESSAGE)   
    print("\n")
    Authentication()  

else:
    logger.debug(Config.WRONG_FILE_RUNNED)