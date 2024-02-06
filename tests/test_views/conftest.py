import hashlib
import pytest
from db.database_operations import create_table,write_to_database,Config,delete_data


@pytest.fixture(scope='package',autouse = True)
def create_testdb(package_mocker):
    package_mocker.patch.object(Config, "DATABASE_NAME", "test_db.db")
    create_table(Config.QUERY_FOR_CREATE_AUTH_TABLE)
    create_table(Config.QUERY_FOR_CREATE_HELPDESK_DETAILS_TABLE)
    create_table(Config.QUERY_FOR_CREATE_BOOKINGS_TABLE)
    create_table(Config.QUERY_FOR_CREATE_ROOMS_DETAILS_TABLE)


@pytest.fixture(scope='package',autouse=True)
def insert_into_table():
    
    q1 = 'INSERT INTO authentication (user_id,username,password,role,pwd_changed) VALUES(?,?,?,?,?)'
    pa = 'Chetna@12'
    pr1= 'Diya@12'
    pr2 = 'Raj@12'

    hashed_passworda = hashlib.sha256(pa.encode()).hexdigest()
    hashed_passwordr1 = hashlib.sha256(pr1.encode()).hexdigest()
    hashed_passwordr2 = hashlib.sha256(pr2.encode()).hexdigest()


    d1 = ('1234','chetna',hashed_passworda,'admin',1)
    d2 = ('2719','diya',hashed_passwordr1,'receptionist',1)
    d3= ('3214','raj',hashed_passwordr2,'receptionist',1)
    write_to_database(q1,d1)
    write_to_database(q1,d2)
    write_to_database(q1,d3)


    q2 = 'INSERT INTO rooms_details (room_id,room_type,room_price,room_status) VALUES (?,?,?,?)'
    r1 = ('2313','AC',2000,'available')
    r2 = ('3713','Non-AC',1500,'unavailable')
    r3 = ('4313','AC',2000,'available')

    write_to_database(q2,r1)
    write_to_database(q2,r2)
    write_to_database(q2,r3)


    q3 = ' INSERT INTO helpdesk_details(emp_id,emp_email,emp_age,emp_phone,emp_gender)VALUES(?,?,?,?,?)'
    h1 = ('2719','diya@gmail.com',25,9825763220,'female')
    h2 = ('3214','raj@gmail.com',23,8782626199,'male')
    write_to_database(q3,h1)
    write_to_database(q3,h2)
    
    q4 = 'INSERT into bookings(g_id,g_name,g_email,g_phone,g_adrs,room_id,check_in_date,check_out_date)VALUES(?,?,?,?,?,?,?,?)'
    b4 = ('6723','sonal','sonal@gmail.com',8782656203,'jaipur',3713,'06-02-2024','08-02-2024')

    write_to_database(q4,b4)
    yield
    delete_data('DELETE from authentication')
    delete_data('DELETE from rooms_details')
    delete_data('DELETE from helpdesk_details')
    delete_data('DELETE from bookings')
    