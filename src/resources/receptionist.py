from fastapi import APIRouter,HTTPException,Depends
from starlette import status
from models.schemas import CheckinSchema,CheckoutSchema,ReceptionistSchema,ChangeDefaultPasswordSchema,ChangeEmpDetailsSchema
from controllers.receptionist_controllers import Receptionist
from controllers.admin_controllers import Admin
from utils.config_class import Config
from resources.auth import get_current_user
from typing import Annotated
from sqlite3 import Error
import logging

recep_router =APIRouter(prefix='/receptionist',
                       tags=['receptionist'])

user_dependency = Annotated[dict,Depends(get_current_user)]

logger = logging.getLogger(__name__)

@recep_router.post("/checkin")
def checkin(data:CheckinSchema,user:user_dependency):
    logger.info(f'Receptionist {user}is Checking in the guest')
    try:
        if user['role']!= Config.RECEPTIONIST:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=Config.UNAUTHORIZED_USER)
        Receptionist.checkin(data.g_name,data.g_email,data.g_phone,data.g_adrs,data.room_id,data.check_out_date)
        return {'message': Config.SUCCESSFUL_CHECKIN}
    except Exception as e:
        raise e


@recep_router.delete("/checkout/{g_id}")
def checkout(user:user_dependency,g_id:int = CheckoutSchema):
    logger.info(f'Receptionist {user}is Checking out the guest {g_id}')
    try:
        if user['role']!= Config.RECEPTIONIST:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=Config.UNAUTHORIZED_USER)
        Receptionist.checkout(g_id)
        return {'message': Config.SUCCESSFUL_CHECKOUT}
    except Error as e:
        raise e


@recep_router.get("/myinfo/{emp_id}") 
def receptionist_info(emp_id: int, user:user_dependency):
    logger.info(f'Receptionist {user}is viewing his/her profile')
    try:
        print(user)
        if user['role']!= Config.RECEPTIONIST:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=Config.UNAUTHORIZED_USER)
        e = Admin.getrecep(emp_id)
        if not e :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        data = Receptionist.recep_details(emp_id)
        return data        
    except Exception as e:
        raise e


@recep_router.get("/available-rooms")   
def view_available_rooms(user:user_dependency):
    logger.info(f'Receptionist {user}is viewing all available rooms in the hotel')
    try:
        if user['role']!= Config.RECEPTIONIST:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=Config.UNAUTHORIZED_USER)
        rooms = Receptionist.view_available_rooms()
        return rooms
    except Exception as e:
        raise e


@recep_router.put("/change-default-pswd")
def change_default_pswd(data:ChangeDefaultPasswordSchema,user:user_dependency):
    logger.info(f'Receptionist {user}is changing his/her default password')
    try:
        if user['role']!= Config.RECEPTIONIST:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=Config.UNAUTHORIZED_USER)
        Receptionist.change_default_password(user['user_id'],data.old_pswd,data.new_pswd)
        return {'message': Config.DEFAULT_PASSWORD_CHANGED}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.OLD_PASSWORD_INCORRECT)
    

@recep_router.put("/update-myinfo")#working
def update_details(data:ChangeEmpDetailsSchema,user:user_dependency):
    logger.info(f'Receptionist {user}is updating his/her details')

    try:
        if user['role']!= Config.RECEPTIONIST:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=Config.UNAUTHORIZED_USER)
        emp_id = user['user_id']
        email = data.email
        age = data.age
        phone = data.phone
        Receptionist.update_my_details(emp_id,email,age,phone)
        return{'message': Config.DETAILS_UPDATED}
    except Exception as e :
        raise e 