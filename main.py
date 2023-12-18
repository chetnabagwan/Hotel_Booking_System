import logging
from authentication.authentication import Authentication
from utils.config_class import Config

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    level = logging.DEBUG,
                    filename = 'logs.txt')
logger = logging.getLogger('main') 

@Config.config_loader
def start():
    logger.info(Config.WELCOME_LOGGING_INFO)
    print(Config.WELCOME_MESSAGE)   
    Authentication()  

if __name__ == '__main__':
    start()