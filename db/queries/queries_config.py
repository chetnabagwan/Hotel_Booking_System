import yaml
F_PATH_ADMIN_QUERIES = 'db\\queries\\queries_base_admin.yml'
F_PATH_EMP_QUERIES = 'db\\queries\\queries_base_receptionist.yml'

class QueriesConfig:
    """
    Maintains all the config variables
    """
    @classmethod
    def loadAdminQueries(cls):
        with open(F_PATH_ADMIN_QUERIES, 'r') as f:
            data = yaml.safe_load(f)
            cls.QUERY_FOR_CREATE_AUTH_TABLE = data['QUERY_FOR_CREATE_AUTH_TABLE']
            cls.QUERY_FOR_CREATE_HELPDESK_DETAILS_TABLE= data['QUERY_FOR_CREATE_HELPDESK_DETAILS_TABLE']
            cls.QUERY_TO_ADD_IN_AUTH_TABLE = data['QUERY_TO_ADD_IN_AUTH_TABLE']
            cls.QUERY_TO_ADD_IN_HELPDESK_DETAILS_TABLE = data['QUERY_TO_ADD_IN_HELPDESK_DETAILS_TABLE']
            cls.QUERY_TO_VERIFY_LOGIN = data['QUERY_TO_VERIFY_LOGIN']
            cls.QUERY_TO_DELETE_FROM_AUTH_TABLE = data['QUERY_TO_DELETE_FROM_AUTH_TABLE']
            cls.QUERY_TO_DEL_RECEPTIONIST = data['QUERY_TO_DEL_RECEPTIONIST']
            cls.QUERY_TO_ENABLE_FOREIGN_KEY = data['QUERY_TO_ENABLE_FOREIGN_KEY']
            cls.QUERY_TO_CHECK_IF_DEFAULT_PASWORD = data['QUERY_TO_CHECK_IF_DEFAULT_PASWORD']
            cls.QUERY_TO_CHANGE_DEFAULT_PASWORD = data['QUERY_TO_CHANGE_DEFAULT_PASWORD']
            cls.QUERY_TO_UPDATE_ROOM_TYPE = data['QUERY_TO_UPDATE_ROOM_TYPE']
            cls.QUERY_TO_UPDATE_ROOM_PRICE = data['QUERY_TO_UPDATE_ROOM_PRICE']
            cls.QUERY_TO_DISPLAY_HOTEL_STATUS= data['QUERY_TO_DISPLAY_HOTEL_STATUS']
            cls.LIST_TO_DISPLAY_ALLRECEPTIONIST_DETAILS = data['LIST_TO_DISPLAY_ALLRECEPTIONIST_DETAILS']
            cls.LIST_TO_DISPLAY_HOTEL_STATUS = data['LIST_TO_DISPLAY_HOTEL_STATUS']
            cls.QUERY_TO_ADD_IN_ROOM_DETAILS_TABLE = data['QUERY_TO_ADD_IN_ROOM_DETAILS_TABLE']
            cls.QUERY_TO_DEL_IN_ROOM_DETAILS_TABLE = data['QUERY_TO_ADD_IN_ROOM_DETAILS_TABLE']


    @classmethod
    def loadReceptionistQueries(cls):
        with open(F_PATH_EMP_QUERIES, 'r') as f:
            data = yaml.safe_load(f)
            cls.QUERY_TO_UPDATE_EMP_MAIL = data['QUERY_TO_UPDATE_EMP_MAIL']
            cls.QUERY_TO_UPDATE_EMP_AGE = data['QUERY_TO_UPDATE_EMP_AGE']
            cls.QUERY_TO_UPDATE_EMP_PHONE = data['QUERY_TO_UPDATE_EMP_PHONE']
            cls.QUERY_TO_UPDATE_EMP_GENDER = data['QUERY_TO_UPDATE_EMP_GENDER']
            cls.LIST_TO_DISPLAY_SELFRECEPTIONIST_DETAILS = data['LIST_TO_DISPLAY_SELFRECEPTIONIST_DETAILS']
