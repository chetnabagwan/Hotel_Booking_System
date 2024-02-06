import logging
from fastapi import FastAPI
from views import auth_views,admin_views,receptionist_views
from starlette.staticfiles import StaticFiles

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s",
    datefmt = "%d-%M-%Y %H:%M:%S", level=logging.DEBUG,
    filename="logs.log")

logger = logging.getLogger(__name__)

app = FastAPI()

logger.info('Application started')


@app.get("/healthy")
def health_check():
    return {'status':'Healthy'}

# app.mount("/static",StaticFiles(directory="static"),name="static")

app.include_router(auth_views.auth_router)
app.include_router(admin_views.admin_router)
app.include_router(receptionist_views.recep_router)

