# from flask import request
from controllers.auth_controller import Authentication
# from flask.views import MethodView
# from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required,get_jwt,get_jti
# from flask_smorest import Blueprint,abort
# from src.blocklist import BLOCKLIST
# from models.schemas import AuthSchema
from fastapi import FastAPI,Path,Query,HTTPException
from pydantic import BaseModel,Field
from typing import Optional
from starlette import status
from fastapi import FastAPI,Body

app =FastAPI()
class AuthRequest(BaseModel):
    username:str = Field(min_length=1)
    password:str = Field(min_length=1)
   
@app.post("/login",status_code=status.HTTP_200_OK)
def post(user_data:AuthRequest):
    data = Authentication.login(user_data['username'],password=['password']) 
    if data:
        return 'Successful login'
    else:
        return "Invalid credentials"

