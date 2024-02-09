from starlette import status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
import logging
from fastapi import Depends,HTTPException
from datetime import datetime,timedelta
from utils.config_class import Config

logger = logging.getLogger(__name__)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

def get_current_user(token:Annotated[str,Depends(oauth2_scheme)]):
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


def create_access_token(user_id:str,role:str,expires_delta:timedelta):
    payload = {'sub':user_id,'role':role}
    expires = datetime.utcnow() + expires_delta
    payload.update({'exp':expires})
    return jwt.encode(payload,Config.SECRET_KEY,algorithm=Config.ALGORITHM)
