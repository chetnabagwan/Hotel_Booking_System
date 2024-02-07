from starlette import status
import logging
from blocklist import BLOCKLIST
from controllers.auth_controller import Authentication
from utils.config_class import Config
from app import app
from fastapi.testclient import TestClient 
import pytest

logger = logging.getLogger(__name__)

auth = TestClient(app)

SAMPLE_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzMjE0Iiwicm9sZSI6InJlY2VwdGlvbmlzdCIsImV4cCI6MTcwNzI4NTY5Mn0.zaWAxcnRCbWAu3IozhNPP0TMsxJ5dNiBewnn7Gc4ElQ"

def test_login_and_gen_token_success():
    request_data ={"username" : "raj",
                   "password" : "Raj@12"}
    response = auth.post("auth/login",json=request_data)
    assert response.json()['access_token'] == SAMPLE_TOKEN
    assert response.json()['token_type']=='Bearer'
    assert response.status_code == status.HTTP_200_OK

def test_login_and_gen_token_invalid():
    request_data ={"username" : "raj",
                   "password" : "Rajj@12"}
    response = auth.post("auth/login",json=request_data)
    assert response.json() == {"detail": Config.INVALID_CREDENTIALS}
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
