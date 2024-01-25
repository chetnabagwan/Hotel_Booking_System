from flask import request
from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required
from flask_smorest import Blueprint, abort
from models.schemas import CheckoutSchema,CheckinSchema,ReceptionistSchema
from controllers.receptionist_controllers import Receptionist
from controllers.admin_controllers import Admin


blp = Blueprint('receptionists',__name__)

@blp.route("/checkin")
class Checkin(MethodView):
    @blp.arguments(CheckinSchema)
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def post(self,data):
        role = get_jwt()['role']
        if role == "receptionist":
            
            Receptionist.checkin()
            return {'message': "Customer is successfully checked-in."}
        
        abort(401, message = "You are not authorized to perform this operation.")



@blp.route("/checkout")
class Checkout(MethodView):
    @blp.arguments(CheckoutSchema)
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def post(self,data):
        role = get_jwt()['role']
        if role == "receptionist":
            
            Receptionist.checkout()
            return {'message': "Customer is successfully checked-out."}
        
        abort(401, message = "You are not authorized to perform this operation.")

@blp.route("/receptionists/<int:emp_id>")
class Receptionist(MethodView):
    @blp.arguments(ReceptionistSchema)
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def get(self,data):
        role = get_jwt()['role']
        if role == "receptionist":
            emp_id=data['emp_id']
            e = Admin.getrecep(emp_id)
            if not e :
                abort(404,message='No receptionist found.')
            
            data = Receptionist.recep_details(emp_id)
            return data
        
        abort(401, message = "You are not authorized to perform this operation.")

    @blp.arguments(ReceptionistSchema)
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def patch(self,data):
        pass