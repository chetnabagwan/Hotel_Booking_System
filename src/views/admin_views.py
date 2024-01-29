from fastapi import APIRouter,HTTPException,Body
from models.schemas import AddRoomSchema,DelRoomSchema
from starlette import status
from models.schemas import AddRoomSchema,RoomUpdateSchema,DelRoomSchema,AddReceptionistSchema,ReceptionistSchema
from controllers.admin_controllers import Admin

admin_router =APIRouter(prefix='/admin',
                       tags=['admin'])

@admin_router.post("/addroom",status_code=status.HTTP_201_CREATED) #working
def addroom(data: AddRoomSchema):
    try:    
        Admin.add_rooms(data.r_type,data.r_price)
        return {'message': 'Room added'}
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@admin_router.delete("/delroom") #working
def delroom(data:DelRoomSchema): 
    try:
        data = dict(data)
        room_no = data["room_no"]
        room = Admin.getroom(room_no)
        
        if room is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Room does not exist")
            
        Admin.del_rooms(room_no)
        return {'message': 'Room deleted'}
    except Exception as e:
        raise e

    
@admin_router.patch("/updateroom") #working
def updateroom(data:RoomUpdateSchema ):
    try:
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


@admin_router.post("/addreceptionist",status_code=status.HTTP_201_CREATED)
def addrecep(data:AddReceptionistSchema):
    try:
        username = data.username
        password = data.password
        emp_email = data.emp_email
        emp_age = data.emp_age
        emp_gender = data.emp_gender
        emp_phone = data.emp_phone
        Admin.add_receptionists(username,password,emp_email,emp_age,emp_gender,emp_phone)
        return {'message': 'Receptionist added'}
    except Exception as e:
        raise e
        # raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@admin_router.delete("/delreceptionist") #working
def delrecep(data:ReceptionistSchema):
    try:
        emp_id = data.emp_id
        emp =  Admin.getrecep(emp_id)
        print(emp)
        if not emp:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Receptionist does not exist")      
        Admin.del_receptionist(emp_id)
        return {'message': 'Receptionist deleted'}
    except Exception as e:
        raise e      


@admin_router.get('/receptionists') #working
def getallreceps():
    try:
        data = Admin.receptionist_info()
        if not data :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No receptionists found")
        return data
    except Exception as e:
        raise e