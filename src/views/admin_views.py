from fastapi import APIRouter,HTTPException, Request
from models.schemas import AddRoomSchema,DelRoomSchema
from starlette import status
from models.schemas import AddRoomSchema,RoomUpdateSchema,DelRoomSchema,AddReceptionistSchema,ReceptionistSchema
from controllers.admin_controllers import Admin
from starlette import status
from typing import Annotated
from fastapi import APIRouter, Depends,HTTPException
from views.auth_views import get_current_user
from utils.config_class import Config
from sqlite3 import Error
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

admin_router =APIRouter(prefix='/admin',
                       tags=['admin'])

templates = Jinja2Templates(directory = "templates")
user_dependency = Annotated[dict,Depends(get_current_user)]

@admin_router.get("/test")
def test(request:Request):
    return templates.TemplateResponse("home.html",{"request": request})

@admin_router.get('/receptionists') #working
def getallreceps(user:user_dependency):
    try:
        if user['role']!= Config.ADMIN:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHORIZED_USER)
        data = Admin.receptionist_info()
        if not data :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=Config.NO_DATA_FOUND)
        return data
    except Exception as e:
        raise e


@admin_router.post("/addreceptionist",status_code=status.HTTP_201_CREATED) #working
def addrecep(data:AddReceptionistSchema,user:user_dependency):
    try:
        if user['role']!= Config.ADMIN:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHORIZED_USER)
        username = data.username
        password = data.password
        emp_email = data.emp_email
        emp_age = data.emp_age
        emp_gender = data.emp_gender
        emp_phone = data.emp_phone
        Admin.add_receptionists(username,password,emp_email,emp_age,emp_gender,emp_phone)
        return {'message': 'Receptionist added'}
    except Error as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=Config.USER_ALREADY_EXIST)
    
    
@admin_router.delete("/delreceptionist") #working
def delrecep(data:ReceptionistSchema,user:user_dependency):
    try:
        if user['role'] != Config.ADMIN:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHORIZED_USER)
        emp_id = data.emp_id
        emp =  Admin.getrecep(emp_id)
        if not emp:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=Config.NO_DATA_FOUND)      
        Admin.del_receptionist(emp_id)
        return {'message': 'Receptionist deleted'}
    except Exception as e:
        raise e      


@admin_router.post("/addroom",status_code=status.HTTP_201_CREATED) #working
def addroom(data: AddRoomSchema,user:user_dependency):
    try: 
        if user['role'] != Config.ADMIN:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHORIZED_USER)   
        Admin.add_rooms(data.r_type,data.r_price)
        return {'message': 'Room added'}
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@admin_router.delete("/delroom") #working
def delroom(data:DelRoomSchema,user:user_dependency): 
    try:
        if user['role'] != Config.ADMIN:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHORIZED_USER)
        room_no = data.room_no
        room = Admin.getroom(room_no)
        if room is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=Config.NO_DATA_FOUND)
        Admin.del_rooms(room_no)
        return {'message': 'Room deleted'}
    except Exception as e:
        raise e

    
@admin_router.put("/updateroom") #working
def updateroom(data:RoomUpdateSchema,user:user_dependency):
    try:
        if user['role'] != Config.ADMIN:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHORIZED_USER)
        room_no = data.room_no
        r_type = data.r_type
        r_price = data.r_price
        room = Admin.getroom(room_no)
        if room is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)    
        Admin.update_rooms_info(r_type,r_price,room_no)
        return{'message': f'Room no {room_no} is updated.'}
    except Exception as e:
        raise e



