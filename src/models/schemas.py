from pydantic import BaseModel,Field
from fastapi import Path,Query

class AuthLoginRequest(BaseModel):
    username:str = Field(min_length=1)
    password:str = Field(min_length=1)

class AuthLoginResponse(BaseModel):
    access_token:str
    token_type:str
class AddRoomSchema(BaseModel):
    r_type:str 
    r_price:int 

class DelRoomSchema(BaseModel):
    room_no:int
class RoomUpdateSchema(BaseModel):
    room_no:int
    r_type:str
    r_price:int

class AddReceptionistSchema(BaseModel):
    username:str
    password:str
    emp_email:str
    emp_age:int
    emp_phone:int
    emp_gender:str

class ReceptionistSchema(BaseModel):
    emp_id:int = Query

class CheckinSchema(BaseModel):
    pass

class CheckoutSchema(BaseModel):
    pass

class ChangeDefaultPasswordSchema(BaseModel):
    old_pswd:str
    new_pswd:str