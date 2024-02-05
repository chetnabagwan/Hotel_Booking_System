from fastapi.testclient import TestClient 
from app import app
from fastapi import status
from views.auth_views import get_current_user

admin = TestClient(app)

def override_user_dependency():
    return {'role':"admin",'user_id':3324}

app.dependency_overrides[get_current_user] = override_user_dependency

def test_getallreceps():
    response = admin.get("/admin/receptionists")
    assert response.status_code == status.HTTP_200_OK

def test_addreceptionist():
    response = admin.post("/addreceptionist")
    assert response.status_code == status.HTTP_201_CREATED