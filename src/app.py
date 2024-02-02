from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from views import auth_views,admin_views,receptionist_views
from starlette.staticfiles import StaticFiles

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

@app.get("/healthy")
def health_check():
    return {'status':'Healthy'}

app.mount("/static",StaticFiles(directory="static"),name="static")

app.include_router(auth_views.auth_router)
app.include_router(admin_views.admin_router)
app.include_router(receptionist_views.recep_router)

