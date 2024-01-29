from datetime import datetime,timedelta
from controllers.auth_controller import Authentication
from fastapi import APIRouter,Path,Query,HTTPException
from models.schemas import AuthLoginRequest,AuthLoginResponse
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt,JWTError

auth_router =APIRouter(prefix='/auth',
                       tags=['auth'])

SECRET_KEY = 'fIqrMcrIKjZqsEZdfwne82n8YsL6F3K0'
ALGORITHM = 'HS256'

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/login')



def create_access_token(username:str,expires_delta:timedelta):
    encode = {'sub':username}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)

@auth_router.post("/verify_token")
async def get_current_user_verify_jwt(token,oauth2_bearer):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str = payload.get('sub')
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid User/token')    
        return payload
        # user_id:int = payload.get('id')
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid User/token')


@auth_router.post("/login",response_model=AuthLoginResponse,status_code=status.HTTP_200_OK)
def post(user_data:AuthLoginRequest):
    data = Authentication.login(user_data['username'],password=['password']) 
    if data:
        token = create_access_token(user_data['username'],timedelta(minutes=15))
        return {'access_token':token,'token_type':'bearer'}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid User/token')



