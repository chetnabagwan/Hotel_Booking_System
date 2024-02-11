from starlette import status
from typing import Annotated
import logging
from fastapi import APIRouter, Depends,HTTPException
from datetime import timedelta
from blocklist import BLOCKLIST
from controllers.auth_controller import Authentication
from utils.config_class import Config
from resources.token_handler import create_access_token,get_current_user,oauth2_scheme
from models.schemas import AuthLoginRequest

auth_router =APIRouter(prefix='/auth',
                       tags=['auth'])


logger = logging.getLogger(__name__)


@auth_router.post("/login",status_code=status.HTTP_200_OK)
def login_and_gen_token(user_data:AuthLoginRequest):
    logger.info(f'User with username : {user_data.username} trying to login into the application')
    try:
        data = Authentication.login(user_data.username,user_data.password)    
        if data :
            token = create_access_token(str(data[0]),data[1],timedelta(minutes=15))
            return {'access_token':token,'token_type':'Bearer'}
    except :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.INVALID_CREDENTIALS)


@auth_router.post("/logout",status_code=status.HTTP_200_OK)
async def logout(token:Annotated[str,Depends(oauth2_scheme)],user:Annotated[dict,Depends(get_current_user)]):
        if user['user_id'] is None or user['role'] is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHENTICATED)  
        BLOCKLIST.add(token)
        return {'message': 'User logged out successfully'}


