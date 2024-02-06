from pydantic import BaseModel,Field,ConfigDict,FutureDate
from fastapi import Path
from datetime import date, datetime

class AuthLoginRequest(BaseModel):
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)

class AuthLoginResponse(BaseModel):
    access_token: str
    token_type: str
class AddRoomSchema(BaseModel):
    r_type: str 
    r_price: int 

class DelRoomSchema(BaseModel):
    room_no: int
class RoomUpdateSchema(BaseModel):
    room_no: int
    r_type: str
    r_price: int

class AddReceptionistSchema(BaseModel):
    username: str
    password: str
    emp_email: str
    emp_age: int
    emp_phone: int
    emp_gender: str

class ReceptionistSchema(BaseModel):
    emp_id: int = Path

class CheckinSchema(BaseModel):
    g_name: str
    g_email: str
    g_phone: int 
    g_adrs : str
    room_id: int 
    check_out_date: FutureDate

class CheckoutSchema(BaseModel):
    g_id: int = Path

class ChangeDefaultPasswordSchema(BaseModel):
    old_pswd: str
    new_pswd: str

class ChangeEmpDetailsSchema(BaseModel):
    email: str
    age: int
    phone: int
