from fastapi.testclient import TestClient 
from app import app
from fastapi import status
from resources.admin import get_current_user
from utils.config_class import Config
import pytest

def override_user_dependency():
    return {'role':"admin",'user_id':1234}


admin = TestClient(app)

@pytest.fixture(scope="module",autouse=True)
def dependency_overrides():
    admin.app.dependency_overrides[get_current_user] = override_user_dependency


def test_getallreceps():
    response = admin.get("/admin/receptionists")
    assert response.status_code == status.HTTP_200_OK


def test_addroom():
    request_data ={"r_type":'AC',
                   "r_price":2000}
    response = admin.post("/admin/addroom",json=request_data)
    
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"message": Config.ROOM_ADDED}


def test_delroom():
    request_data ={"room_no":2313}
    response = admin.request("DELETE","/admin/delroom",json = request_data)
    assert response.status_code == status.HTTP_200_OK


def test_addrecep():
    request_data = {
  "username": "riya",
  "password": "Riya@12",
  "emp_email": "riya@gmail.com",
  "emp_age": 35,
  "emp_phone": 9825425620,
  "emp_gender": "female"}
    response =  admin.post("admin/addreceptionist",json= request_data)
    assert response.status_code == status.HTTP_201_CREATED


def test_delrecep():
    response = admin.request("DELETE","admin/delreceptionist/2719")
    assert response.json() == {"message": Config.RECEPTIONIST_DELETED}


def test_delrecep_notfound():
    response = admin.request("DELETE","admin/delreceptionist/2729")
    assert response.json() == {"detail": Config.NO_DATA_FOUND}
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_updateroom():
    request_data ={"room_no":3713,
                   "r_type":'AC',
                   "r_price":2000
                   }
    response = admin.request("PUT","/admin/updateroom",json = request_data)
    assert response.status_code == status.HTTP_200_OK


def test_view_all_bookings():
    response = admin.get("admin/bookings")
    assert response.status_code == status.HTTP_200_OK
