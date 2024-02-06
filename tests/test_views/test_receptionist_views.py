from fastapi.testclient import TestClient 
from app import app
from fastapi import status
from views.receptionist_views import get_current_user
from utils.config_class import Config

receptionist = TestClient(app)

def override_user_dependency():
    return {'role':"receptionist",'user_id':2719}

receptionist.app.dependency_overrides[get_current_user] = override_user_dependency

