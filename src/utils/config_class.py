import yaml
import os

# FPATH_PROMPTS = 'yml_files\\prompts.yml'
# FPATH_PRINT_STATEMENTS = 'yml_files\\print_statements.yml'
# FPATH_LOGGING_STATEMENTS = 'yml_files\\logging_statements.yml'
# F_PATH_ADMIN_QUERIES = 'yml_files\\admin_queries.yml'
# F_PATH_EMP_QUERIES = 'yml_files\\receptionist_queries.yml'

path_current_directory = os.path.dirname(__file__)
FPATH_PROMPTS = os.path.join(path_current_directory, '../yml_files/prompts.yml')
FPATH_PRINT_STATEMENTS = os.path.join(path_current_directory, '../yml_files/print_statements.yml')
FPATH_LOGGING_STATEMENTS = os.path.join(path_current_directory, '../yml_files/logging_statements.yml')
F_PATH_ADMIN_QUERIES = os.path.join(path_current_directory, '../yml_files/admin_queries.yml')
F_PATH_EMP_QUERIES = os.path.join(path_current_directory, '../yml_files/receptionist_queries.yml')


class Config :
    """
    Maintains all the config variables
    """
    ADMIN_PROMPT = None
    RECEPTIONIST_PROMPT = None
    ADMIN = None
    RECEPTIONIST = None

    UPDATE_ROOMS_DETAILS_PROMPT = None
    ATTEMPTS = None
    WD_REGEX = None
    GEN_REGEX = None
    PHONE_NUMBER_REGEX = None
    DATABASE_NAME = None  
    ALGORITHM = None
    SECRET_KEY = None

    WELCOME_MESSAGE =None 
    ROW_NOT_EXISTS_MESSAGE = None
    WRONG_INPUT_ENTERED_MESSAGE = None
    PRINT_USERNAME = None 
    PRINT_PASSWORD = None
    ENTER_STRONG_PASSWORD = None
    ENTER_GENDER = None   
    ENTER_PHONE_NO = None
    ENTER_MAIL = None
    ENTER_AGE = None
    ENTER_ROLE =  None
    WELCOME_ADMIN_MESSAGE =None
    ENTER_EMP_ID = None
    ENTER_DEFAULT_PASSWORD = None
    ENTER_NEW_PASSWORD = None
    CONFIRM_PASSWORD = None
    PRINT_LOGIN =   None
    LOGIN_FAILED = None
    PASSWORD_REQUIREMENTS = None
    UNAUTHORIZED_USER = None
    NO_DATA_FOUND = None
    OLD_PASSWORD_INCORRECT = None

    WELCOME_LOGGING_INFO = None
    WRONG_FILE_RUNNED = None
    REGISTERED_SUCCESSFULLY = None
    DELETED_SUCCESSFULLY = None
    UPDATED_SUCCESSFULLY = None
    LOGGED_IN = None
    ERROR_MESSAGE = None
    ROOM_ADDED = None
    ROOM_DELETED = None
    INVALID_CREDENTIALS = None
    UNAUTHENTICATED = None
    USER_ALREADY_EXIST = None
    SUCCESSFUL_CHECKIN =None
    SUCCESSFUL_CHECKOUT = None
    DEFAULT_PASSWORD_CHANGED = None
    RECEPTIONIST_ADDED = None
    RECEPTIONIST_DELETED = None
    DETAILS_UPDATED = None

    QUERY_FOR_CREATE_AUTH_TABLE = None
    QUERY_FOR_CREATE_HELPDESK_DETAILS_TABLE = None
    QUERY_FOR_CREATE_ROOMS_DETAILS_TABLE = None
    QUERY_FOR_CREATE_BOOKINGS_TABLE =None
    QUERY_TO_ADD_IN_AUTH_TABLE = None
    QUERY_TO_ADD_IN_HELPDESK_DETAILS_TABLE = None
    QUERY_TO_VERIFY_LOGIN = None
    QUERY_TO_DELETE_FROM_AUTH_TABLE = None
    QUERY_TO_DEL_RECEPTIONIST = None
    QUERY_TO_ENABLE_FOREIGN_KEY = None
    QUERY_TO_CHECK_IF_DEFAULT_PASWORD = None
    QUERY_TO_CHANGE_DEFAULT_PASSWORD = None
    QUERY_TO_UPDATE_ROOM_DETAILS = None
    QUERY_TO_DISPLAY_HOTEL_STATUS = None
    LIST_TO_DISPLAY_ALLRECEPTIONIST_DETAILS = None
    QUERY_TO_ADD_IN_ROOM_DETAILS_TABLE = None
    QUERY_TO_DEL_IN_ROOM_DETAILS_TABLE = None
    QUERY_TO_VIEW_ALL_BOOKINGS = None
    QUERY_TO_UPDATE_EMP_DEATILS = None
    QUERY_TO_FETCH_PASSWORD_FROM_AUTH = None
    LIST_TO_DISPLAY_SELFRECEPTIONIST_DETAILS = None
    QUERY_TO_FETCH_ALL_AVAILABLE_ROOMS = None
    QUERY_FOR_CHECKIN = None
    QUERY_FOR_CHECKOUT = None
    QUERY_TO_CHANGE_ROOM_STATUS = None
    QUERY_TO_GET_ROOMID_FROM_GUESTID = None


    @classmethod
    def load(cls):
        with open(FPATH_PROMPTS, 'r') as f:
            data = yaml.safe_load(f)
            cls.ADMIN_PROMPT = data['ADMIN_PROMPT']
            cls.ADMIN = data['ADMIN']
            cls.RECEPTIONIST=  data['RECEPTIONIST']
            cls.RECEPTIONIST_PROMPT = data['RECEPTIONIST_PROMPT']
            cls.UPDATE_ROOMS_DETAILS_PROMPT = data['UPDATE_ROOMS_DETAILS_PROMPT']
            cls.ATTEMPTS = data['ATTEMPTS']
            cls.PWD_REGEX = data['PWD_REGEX']
            cls.GEN_REGEX = data['GEN_REGEX']
            cls.PHONE_NUMBER_REGEX = data['PHONE_NUMBER_REGEX']
            cls.DATABASE_NAME = data['DATABASE_NAME']
            cls.SECRET_KEY = data['SECRET_KEY']
            cls.ALGORITHM = data['ALGORITHM']

    @classmethod
    def load_print_statements(cls):
        with open(FPATH_PRINT_STATEMENTS,'r') as f:
            data = yaml.safe_load(f)           
            cls.WELCOME_MESSAGE = data['WELCOME_MESSAGE']
            cls.ROW_NOT_EXISTS_MESSAGE = data['ROW_NOT_EXISTS_MESSAGE']
            cls.WRONG_INPUT_ENTERED_MESSAGE = data['WRONG_INPUT_ENTERED_MESSAGE']
            cls.PRINT_USERNAME = data['PRINT_USERNAME']
            cls.PRINT_PASSWORD = data['PRINT_PASSWORD']
            cls.ENTER_STRONG_PASSWORD = data['ENTER_STRONG_PASSWORD']
            cls.ENTER_GENDER = data['ENTER_GENDER']
            cls.ENTER_PHONE_NO = data['ENTER_PHONE_NO']
            cls.ENTER_MAIL = data['ENTER_MAIL']
            cls.ENTER_AGE = data['ENTER_AGE']
            cls.ENTER_ROLE = data['ENTER_ROLE']
            cls.WELCOME_ADMIN_MESSAGE = data['WELCOME_ADMIN_MESSAGE']
            cls.ENTER_EMP_ID = data['ENTER_EMP_ID']
            cls.ENTER_DEFAULT_PASSWORD = data['ENTER_DEFAULT_PASSWORD']
            cls.ENTER_NEW_PASSWORD = data['ENTER_NEW_PASSWORD']
            cls.CONFIRM_PASSWORD = data['CONFIRM_PASSWORD'] 
            cls.PRINT_LOGIN = data['PRINT_LOGIN']
            cls.LOGIN_FAILED = data['LOGIN_FAILED']
            cls.PASSWORD_REQUIREMENTS = data['PASSWORD_REQUIREMENTS']
            cls.UNAUTHORIZED_USER = data['UNAUTHORIZED_USER']
            cls.NO_DATA_FOUND = data['NO_DATA_FOUND']
            cls.UNAUTHENTICATED= data['UNAUTHENTICATED']
            cls.INVALID_CREDENTIALS = data['INVALID_CREDENTIALS']
            cls.USER_ALREADY_EXIST = data['USER_ALREADY_EXIST']
            cls.SUCCESSFUL_CHECKIN = data['SUCCESSFUL_CHECKIN']
            cls.SUCCESSFUL_CHECKOUT = data['SUCCESSFUL_CHECKOUT']
            cls.DEFAULT_PASSWORD_CHANGED = data['DEFAULT_PASSWORD_CHANGED']
            cls.RECEPTIONIST_ADDED = data['RECEPTIONIST_ADDED']
            cls.RECEPTIONIST_DELETED = data['RECEPTIONIST_DELETED']
            cls.ROOM_ADDED = data['ROOM_ADDED']
            cls.ROOM_DELETED = data['ROOM_DELETED'] 
            cls.DETAILS_UPDATED = data['DETAILS_UPDATED']
            cls.OLD_PASSWORD_INCORRECT = data['OLD_PASSWORD_INCORRECT']

    @classmethod
    def load_logging_statements(cls):
        with open(FPATH_LOGGING_STATEMENTS,'r') as f:
            data = yaml.safe_load(f)
            cls.WELCOME_LOGGING_INFO = data['WELCOME_LOGGING_INFO']
            cls.WRONG_FILE_RUNNED = data['WRONG_FILE_RUNNED']
            cls.REGISTERED_SUCCESSFULLY = data['REGISTERED_SUCCESSFULLY']
            cls.DELETED_SUCCESSFULLY = data['DELETED_SUCCESSFULLY']
            cls.UPDATED_SUCCESSFULLY = data['UPDATED_SUCCESSFULLY']
            cls.LOGGED_IN = data['LOGGED_IN']
            cls.ERROR_MESSAGE = data['ERROR_MESSAGE']
          

    @classmethod
    def loadAdminQueries(cls):
        with open(F_PATH_ADMIN_QUERIES, 'r') as f:
            data = yaml.safe_load(f)
            cls.QUERY_FOR_CREATE_AUTH_TABLE = data['QUERY_FOR_CREATE_AUTH_TABLE']
            cls.QUERY_FOR_CREATE_HELPDESK_DETAILS_TABLE = data['QUERY_FOR_CREATE_HELPDESK_DETAILS_TABLE']
            cls.QUERY_FOR_CREATE_ROOMS_DETAILS_TABLE = data['QUERY_FOR_CREATE_ROOMS_DETAILS_TABLE']
            cls.QUERY_FOR_CREATE_BOOKINGS_TABLE = data['QUERY_FOR_CREATE_BOOKINGS_TABLE']
            cls.QUERY_TO_ADD_IN_AUTH_TABLE = data['QUERY_TO_ADD_IN_AUTH_TABLE']
            cls.QUERY_TO_ADD_IN_HELPDESK_DETAILS_TABLE = data['QUERY_TO_ADD_IN_HELPDESK_DETAILS_TABLE']
            cls.QUERY_TO_FETCH_RECEPTIONIST = data['QUERY_TO_FETCH_RECEPTIONIST']
            cls.QUERY_TO_VERIFY_LOGIN = data['QUERY_TO_VERIFY_LOGIN']
            cls.QUERY_TO_DELETE_FROM_AUTH_TABLE = data['QUERY_TO_DELETE_FROM_AUTH_TABLE']
            cls.QUERY_TO_DEL_RECEPTIONIST = data['QUERY_TO_DEL_RECEPTIONIST']
            cls.QUERY_TO_ENABLE_FOREIGN_KEY = data['QUERY_TO_ENABLE_FOREIGN_KEY']
            cls.QUERY_TO_CHECK_IF_DEFAULT_PASWORD = data['QUERY_TO_CHECK_IF_DEFAULT_PASWORD']
            cls.QUERY_TO_UPDATE_ROOM_DETAILS = data['QUERY_TO_UPDATE_ROOM_DETAILS']
            cls.QUERY_TO_FETCH_ROOM = data['QUERY_TO_FETCH_ROOM']
            cls.QUERY_TO_DISPLAY_HOTEL_STATUS= data['QUERY_TO_DISPLAY_HOTEL_STATUS']
            cls.QUERY_TO_DISPLAY_ALLRECEPTIONIST_DETAILS = data['QUERY_TO_DISPLAY_ALLRECEPTIONIST_DETAILS']
            cls.LIST_TO_DISPLAY_ALLRECEPTIONIST_DETAILS = data['LIST_TO_DISPLAY_ALLRECEPTIONIST_DETAILS']
            cls.LIST_TO_DISPLAY_HOTEL_STATUS = data['LIST_TO_DISPLAY_HOTEL_STATUS']
            cls.QUERY_TO_ADD_IN_ROOM_DETAILS_TABLE = data['QUERY_TO_ADD_IN_ROOM_DETAILS_TABLE']
            cls.QUERY_TO_DEL_IN_ROOM_DETAILS_TABLE = data['QUERY_TO_DEL_IN_ROOM_DETAILS_TABLE']
            cls.QUERY_TO_VIEW_ALL_BOOKINGS = data['QUERY_TO_VIEW_ALL_BOOKINGS']


    @classmethod
    def loadReceptionistQueries(cls):
        with open(F_PATH_EMP_QUERIES, 'r') as f:
            data = yaml.safe_load(f)
            cls.QUERY_TO_UPDATE_EMP_DETAILS = data['QUERY_TO_UPDATE_EMP_DETAILS']
            cls.QUERY_TO_DISPLAY_SELFRECEPTIONIST_DETAILS = data['QUERY_TO_DISPLAY_SELFRECEPTIONIST_DETAILS'] 
            cls.QUERY_TO_FETCH_PASSWORD_FROM_AUTH = data['QUERY_TO_FETCH_PASSWORD_FROM_AUTH']
            cls.QUERY_TO_CHANGE_DEFAULT_PASSWORD = data['QUERY_TO_CHANGE_DEFAULT_PASSWORD']
            cls.QUERY_FOR_CHECKIN = data['QUERY_FOR_CHECKIN']
            cls.QUERY_FOR_CHECKOUT = data['QUERY_FOR_CHECKOUT']
            cls.QUERY_TO_GET_ROOMID_FROM_GUESTID = data['QUERY_TO_GET_ROOMID_FROM_GUESTID']
            cls.QUERY_TO_CHANGE_ROOM_STATUS = data['QUERY_TO_CHANGE_ROOM_STATUS']
            cls.QUERY_TO_FETCH_ALL_AVAILABLE_ROOMS =data['QUERY_TO_FETCH_ALL_AVAILABLE_ROOMS']
    
Config.load()
Config.load_print_statements()
Config.load_logging_statements()
Config.loadAdminQueries()
Config.loadReceptionistQueries() 

    

   
