from fastapi import APIRouter,HTTPException,Body
from starlette import status
from models.schemas import CheckinSchema,CheckoutSchema,ReceptionistSchema
from controllers.receptionist_controllers import Receptionist
from controllers.admin_controllers import Admin


recep_router =APIRouter(prefix='/receptionist',
                       tags=['receptionist'])


@recep_router.post("/checkin")
def checkin(data:CheckinSchema = Body()):
    Receptionist.checkin(data)
    return {'message': "Customer is successfully checked-in."}


@recep_router.post("/checkout")
def checkout(data:CheckoutSchema = Body()):
    Receptionist.checkout(data)
    return {'message': "Customer is successfully checked-in."}


@recep_router.get("/receptionists")
def receptionist_info(data:ReceptionistSchema=Body()):
    try:
        emp_id=data['emp_id']
        e = Admin.getrecep(emp_id)
        if not e :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        data = Receptionist.recep_details(emp_id)
        return data
        
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Receptionist does not exist")