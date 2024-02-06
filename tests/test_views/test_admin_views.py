from fastapi.testclient import TestClient 
from app import app
from fastapi import status
from views.admin_views import get_current_user
from utils.config_class import Config
import pytest

def override_user_dependency():
    return {'role':"admin",'user_id':1234}


admin = TestClient(app)

@pytest.fixture(scope="module")
def dependency_overrides():
    admin.app.dependency_overrides[get_current_user] = override_user_dependency


def test_getallreceps(dependency_overrides):
    response = admin.get("/admin/receptionists")
    assert response.status_code == status.HTTP_200_OK


def test_addroom(dependency_overrides):
    request_data ={"r_type":'AC',
                   "r_price":2000}
    response = admin.post("/admin/addroom",json=request_data)
    
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"message": Config.ROOM_ADDED}


def test_delroom(dependency_overrides):
    request_data ={"room_no":2313}
    response = admin.request("DELETE","/admin/delroom",json = request_data)
    assert response.status_code == status.HTTP_200_OK


def test_delrecep(dependency_overrides):
    request_data ={"emp_id" : 2719}
    response = admin.request("DELETE","/admin/delreceptionist",json = request_data)
    assert response.json() == {"message": Config.RECEPTIONIST_DELETED}


def test_updateroom(dependency_overrides):
    request_data ={"room_no":3713,
                   "r_type":'AC',
                   "r_price":2000
                   }
    response = admin.request("PUT","/admin/updateroom",json = request_data)
    assert response.status_code == status.HTTP_200_OK

