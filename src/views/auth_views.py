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

def create_access_token(user_id:str,role:str,expires_delta:timedelta):
    payload = {'sub':user_id,'role':role}
    expires = datetime.utcnow() + expires_delta
    payload.update({'exp':expires})
    return jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)


@auth_router.post("/login",status_code=status.HTTP_200_OK) #working
def login_and_gen_token(user_data: OAuth2PasswordRequestForm=Depends()):
    try:
        data = Authentication.login(user_data.username,user_data.password) 
       
        if data :
            token = create_access_token(str(data[0]),data[1],timedelta(minutes=15))
            return {'access_token':token,'token_type':'Bearer'}
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.INVALID_CREDENTIALS)


async def get_current_user(token:Annotated[str,Depends(oauth2_scheme)]):
    print(token)
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        user_id = payload.get('sub')
        role:str = payload.get('role')
        if user_id is None or role is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHENTICATED_USER)  
        return {'role':role,'user_id':user_id  }
    except JWTError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=Config.UNAUTHENTICATED_USER)

