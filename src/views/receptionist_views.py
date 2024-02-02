from fastapi import APIRouter,HTTPException,Depends
from starlette import status
from models.schemas import CheckinSchema,CheckoutSchema,ReceptionistSchema,ChangeDefaultPasswordSchema,ChangeEmpDetailsSchema
from controllers.receptionist_controllers import Receptionist
from controllers.admin_controllers import Admin
from utils.config_class import Config
from views.auth_views import get_current_user
from typing import Annotated
from sqlite3 import Error

recep_router =APIRouter(prefix='/receptionist',
                       tags=['receptionist'])

user_dependency = Annotated[dict,Depends(get_current_user)]

@recep_router.post("/checkin")
def checkin(data:CheckinSchema,user:user_dependency):
    Receptionist.checkin(data)
    return {'message': "Customer is successfully checked-in."}


@recep_router.post("/checkout")
def checkout(data:CheckoutSchema,user:user_dependency):
    Receptionist.checkout(data)
    return {'message': "Customer is successfully checked-in."}


@recep_router.get("/myinfo/{emp_id}") 
def receptionist_info(user:user_dependency,emp_id:int = ReceptionistSchema):
    try:
        if user['role']!= Config.RECEPTIONIST:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHORIZED_USER)
        e = Admin.getrecep(emp_id)
        if not e :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        data = Receptionist.recep_details(emp_id)
        return data        
    except Exception as e:
        raise e
    
@recep_router.put("/change-default-pswd")
def change_default_pswd(data:ChangeDefaultPasswordSchema,user:user_dependency):
    try:
        if user['role']!= Config.RECEPTIONIST:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHORIZED_USER)
        Receptionist.change_default_password(user['user_id'],data.old_pswd,data.new_pswd)
        return{'message': f'Default password changed'}
    except Exception as e:
        raise e
    
@recep_router.put("/update-myinfo")#working
def update_details(data:ChangeEmpDetailsSchema,user:user_dependency):
    try:
        if user['role']!= Config.RECEPTIONIST:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHORIZED_USER)
        emp_id = user['user_id']
        email = data.email
        age = data.age
        phone = data.phone
        print(phone)
        Receptionist.update_my_details(emp_id,email,age,phone)
        return{'message': f'Receptionist details updated'}
    except Exception as e :
        raise e 