from starlette import status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
import logging
from fastapi import APIRouter, Depends,HTTPException
from datetime import datetime,timedelta
from blocklist import BLOCKLIST
from controllers.auth_controller import Authentication
from utils.config_class import Config

auth_router =APIRouter(prefix='/auth',
                       tags=['auth'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

logger = logging.getLogger(__name__)

def create_access_token(user_id:str,role:str,expires_delta:timedelta):
    payload = {'sub':user_id,'role':role}
    expires = datetime.utcnow() + expires_delta
    payload.update({'exp':expires})
    return jwt.encode(payload,Config.SECRET_KEY,algorithm=Config.ALGORITHM)


@auth_router.post("/login",status_code=status.HTTP_200_OK)
def login_and_gen_token(user_data: OAuth2PasswordRequestForm=Depends()):
    logger.info(f'User with username : {user_data.username} tries to login into the application')
    try:
        data = Authentication.login(user_data.username,user_data.password)    
        if data :
            token = create_access_token(str(data[0]),data[1],timedelta(minutes=15))
            return {'access_token':token,'token_type':'Bearer'}
    except :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.INVALID_CREDENTIALS)


async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token,Config.SECRET_KEY,algorithms=[Config.ALGORITHM])
        user_id = payload.get('sub')
        role:str = payload.get('role')
        if user_id is None or role is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHENTICATED_USER)  
        return {'role':role,'user_id':user_id  }
    except JWTError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHENTICATED_USER)

@auth_router.post("/logout",status_code=status.HTTP_200_OK)
async def logout(token:Annotated[str,Depends(oauth2_scheme)],user:Annotated[dict,Depends(get_current_user)]):
        if user['user_id'] is None or user['role'] is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHENTICATED_USER)  
        BLOCKLIST.add(token)


