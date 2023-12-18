import hashlib
import logging
import sys
from prettytable import PrettyTable
from utils.config_class import Config
from .database_context_manager import DatabaseContextManager

logger = logging.getLogger('database')

def create_table(query) -> None:
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query)

def add_data(query,*args) -> None:
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor() 
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query,*args)

def fetch_user(query,username: str,password: str) -> str:
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute(query,(username,hashed_password))
        record = cursor.fetchone()
        if record == None:
            return None  
        else:
            return (record[3],record[0])        
        
def delete_data(query,emp_id: int) -> None:
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        var = cursor.execute(query,(emp_id,))
        if var.rowcount == 0:
            logging.critical(Config.ERROR_MESSAGE)
            print(Config.ROW_NOT_EXISTS_MESSAGE)
            sys.exit()

def display_data(query,table_schema: list) -> None:
     with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        table = PrettyTable(table_schema)
        for row in cursor.fetchall():
            table.add_row(row)
        print(table)

def update_data(query,*args) -> None:
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()   
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query,*args)  

def display_receptionist_data(query,emp_id: int, table_schema: list):
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        var = cursor.execute(query,(emp_id,))       
        if var.rowcount == 0:
            logging.critical(Config.ERROR_MESSAGE)
        else:
            table = PrettyTable(table_schema)
            row = cursor.fetchone()
            table.add_row(row)
            print(table)    

def fetch_data(query,str) -> list:
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        record = cursor.execute(query,(str,)).fetchone()
        return record[0]