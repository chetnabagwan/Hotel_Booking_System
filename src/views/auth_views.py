from starlette import status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from fastapi import APIRouter, Depends,HTTPException
from datetime import datetime,timedelta
from controllers.auth_controller import Authentication
from utils.config_class import Config

auth_router =APIRouter(prefix='/auth',
                       tags=['auth'])

SECRET_KEY = 'fIqrMcrIKjZqsEZdfwne82n8YsL6F3K0'
ALGORITHM = 'HS256'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

def create_access_token(username:str,role:str,expires_delta:timedelta):
    payload = {'sub':username,'role':role}
    expires = datetime.utcnow() + expires_delta
    payload.update({'exp':expires})
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)


@auth_router.post("/login",status_code=status.HTTP_200_OK)
def login_and_gen_token(user_data: OAuth2PasswordRequestForm=Depends()):
    try:
        data = Authentication.login(user_data.username,user_data.password) 
       
        if data:
            token = create_access_token(user_data.username,data[1],timedelta(minutes=15))
            return {'access_token':token,'token_type':'Bearer'}
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.INVALID_CREDENTIALS)


async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str = payload.get('sub')
        role:str = payload.get('role')
        if username is None or role is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHENTICATED_USER)  
        return role,username  
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHENTICATED_USER)

