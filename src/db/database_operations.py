import logging
from utils.config_class import Config
from .database_context_manager import DatabaseContextManager

logger = logging.getLogger('database')

def create_table(query) -> None:
    print(Config.DATABASE_NAME)
    print("My database: --------------------------------------", Config.DATABASE_NAME)
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query)

def write_to_database(query:str|list,data:tuple|list):
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor() 
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        if isinstance(query,str):
            cursor.execute(query,data)
        else:
            for i in range(len(query)):
                cursor.execute(query[i],data[i])
        connection.commit()

         
def fetch_user(query,username: str,password: str) -> str:
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(query,(username,password,))
        record = cursor.fetchone()
        if record == None:
            return None  
        else:
            return (record[0],record[3])        
        
def display_data(query,*args) -> None:
     print("*"*100, *args)
     with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        data = cursor.execute(query,(*args,)).fetchall()
        return data

def update_data(query,*args) -> None:
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()   
        cursor.execute(Config.QUERY_TO_ENABLE_FOREIGN_KEY)
        cursor.execute(query,*args)  

def fetch_data(query,id:int):
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        record = cursor.execute(query,(id,)).fetchone()
        return record[0]
    
def delete_data(query):
    with DatabaseContextManager(Config.DATABASE_NAME) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
    