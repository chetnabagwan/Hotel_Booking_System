# import pytest
# from db.database_operations import create_table,write_to_database,Config


# @pytest.fixture(scope='package',autouse = True)
# def create_testdb(package_mocker):
#     package_mocker.patch.object(Config,"DATABASE_NAME","test_db")
#     create_table(Config.QUERY_FOR_CREATE_AUTH_TABLE)
#     create_table(Config.QUERY_FOR_CREATE_HELPDESK_DETAILS_TABLE)
#     create_table(Config.QUERY_FOR_CREATE_BOOKINGS_TABLE)
#     create_table(Config.QUERY_FOR_CREATE_ROOMS_DETAILS_TABLE)

      

# @pytest.fixture(scope='package',autouse=True)
# def insert_into_table():
#     write_to_database(Config.QUERY_TO_ADD_IN_AUTH_TABLE)
# #     insert
# #     yield
# #     drop tables