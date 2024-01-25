from flask import request
from controllers.auth_controller import Authentication
from flask.views import MethodView
from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required,get_jwt,get_jti
from flask_smorest import Blueprint,abort
from src.blocklist import BLOCKLIST
from models.schemas import AuthSchema

blp = Blueprint('authentication',__name__)

@blp.post("/login")
class Auth(MethodView):
    @blp.arguments(AuthSchema)
    def post(username,password):
        user_data = request.get_json()
        username = user_data['username']
        password = user_data['password']
        data = Authentication.login(username,password) 
        if data:
            access_token = create_access_token(identity=data[0],additional_claims={"role": data[1]}, fresh=True)
            return {"access_token" : access_token}
        
        abort(401, message="Invalid credentials.")


@blp.post('/logout')
@jwt_required()
def logout_user():
    jti = get_jwt().get('jti')
    BLOCKLIST.add(jti)
    return {'message': 'Successfully logged out'}