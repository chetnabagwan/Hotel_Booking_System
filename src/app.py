from fastapi import FastAPI
from views import auth_views,admin_views,receptionist_views
# from utils.config_class import Config


# # def create_app():
# Config.load(Config)
# Config.load_print_statements(Config)
# Config.load_logging_statements(Config)
# Config.loadAdminQueries(Config)
# Config.loadReceptionistQueries(Config) 
app = FastAPI()

app.include_router(auth_views.auth_router)
app.include_router(admin_views.admin_router)
app.include_router(receptionist_views.recep_router)

# create_app()