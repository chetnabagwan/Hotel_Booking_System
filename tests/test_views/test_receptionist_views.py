from fastapi.testclient import TestClient 
import pytest
from fastapi import status
from views.receptionist_views import get_current_user
from utils.config_class import Config
from app import app

receptionist = TestClient(app)

def override_user_dependency():
    return {'role':"receptionist",'user_id':3214}

@pytest.fixture(scope="module",autouse=True)
def dependency_overrides():
    receptionist.app.dependency_overrides[get_current_user] = override_user_dependency


def test_checkin():
    request_data = {
                    "g_name": "sonu",
                    "g_email": "Sonu@gmail.com",
                    "g_phone": 9981804181,
                    "g_adrs": "Ashta Sehore",
                    "room_id": 4313,
                    "check_out_date": "2024-02-08"
                    }
    response = receptionist.post("receptionist/checkin",json=request_data)
    assert response.json()== {'message': Config.SUCCESSFUL_CHECKIN}


def test_checkout():
    response = receptionist.delete("receptionist/checkout/6723")
    assert response.json() == {'message': Config.SUCCESSFUL_CHECKOUT}


def test_view_available_rooms():
    response = receptionist.get("receptionist/available-rooms")
    assert response.status_code == status.HTTP_200_OK


def test_receptionist_info():
    response = receptionist.get("receptionist/myinfo/3214")
    assert response.status_code == status.HTTP_200_OK


def test_update_details():
    request_data = { "email":"raaj@gmail.com",
                     "age" :25,
                     "phone": 8782626199
                    }
    response =  receptionist.put("receptionist/update-myinfo",json=request_data)
    assert response.json() == {'message': Config.DETAILS_UPDATED}
