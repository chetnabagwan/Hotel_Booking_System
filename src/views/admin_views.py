from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required
from flask_smorest import Blueprint, abort
from models.schemas import AddRoomSchema,RoomUpdateSchema,DelRoomSchema,AddReceptionistSchema,ReceptionistSchema
from controllers.admin_controllers import Admin

blp = Blueprint('admin',__name__)

@blp.route("/addroom")
class AddRoom(MethodView):
    @blp.arguments(AddRoomSchema)
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def post(self,data):
        role = get_jwt()['role']
        if role == "admin":
            r_type = data['r_type']
            r_price = data['r_price']
            Admin.add_rooms(r_type,r_price)
            return {'message': 'Room added'}
        
        abort(401, message = "You are not authorized to perform this operation.")

@blp.route("/delroom/<int:room_no>") #doubt 
class DeleteRoom(MethodView):
    @blp.arguments(DelRoomSchema)
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def delete(self,data):
        role = get_jwt()['role']
        if role == "admin":
            room_no = data['room_no']
            room = Admin.getroom(room_no)
            if not room:
                abort(400,message = "No room found with the given room number.")
            Admin.del_rooms(room_no)
            return {'message': 'Room deleted'}
        
        abort(401, message = "You are not authorized to perform this operation.")

    
@blp.route("/updateroom/<int:room_no>")
class UpdateRoom(MethodView):#doubt
    @blp.arguments(RoomUpdateSchema)
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def patch(self,data):
        role = get_jwt()['role']
        if role == "admin":
            room_no = data['room_no']
            r_type = data['r_type']
            r_price = data['r_price']
            room = Admin.getroom(room_no)
            if not room:
                abort(400,message = "No room found with the given room number.")
           
            Admin.update_rooms_info(room_no,r_type,r_price)
            return{'message': f'Room no{room_no} is updated'}

        abort(401, message = "You are not authorized to perform this operation.")


@blp.route("/addreceptionist")
class AddReceptionist(MethodView):
    @blp.arguments(AddReceptionistSchema)
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def post(self,data):
        username = data['username']
        password = data['password']
        emp_email = data['emp_email']
        emp_age = data['emp_age']
        emp_gender = data['emp_gender']
        emp_phone = data['emp_phone']
        Admin.add_receptionists(username,password,emp_email,emp_age,emp_gender,emp_phone)
        return {'message': 'Receptionist added'}

@blp.route("/delreceptionist/<int:emp_id>")
class DeleteReceptionist(MethodView):
    @blp.arguments(ReceptionistSchema)
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def delete(self,data):
        role = get_jwt()['role']
        if role == "admin":
            emp_id = data['emp_id']
            emp =  Admin.getrecep(emp_id)
            if not emp:
                abort(400,message = "No receptionist found with the given Id.")
            Admin.del_receptionist(emp_id)
            return {'message': 'Receptionist deleted'}
        
        abort(401, message = "You are not authorized to perform this operation.")

@blp.route('/receptionists')
class AllReceptionist(MethodView):
    @jwt_required()
    @blp.doc(parameters=[{'name': 'Authorization', 'in': 'header', 'description': 'Authorization: Bearer <access_token>', 'required': 'true'}])
    def get(self):
        data = Admin.receptionist_info()
        if not data:
            abort(404,message='No receptionists found.')
        return data