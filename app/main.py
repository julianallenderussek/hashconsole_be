from fastapi import FastAPI
from app.controllers import user_controller, project_controller, user_project_role_controller
from app.models.user import User
from app.models.role import Role 
from app.models.project import Project
from app.models.user_project_role import UserProjectRole
from app.database import engine, Base

app = FastAPI()

# Create all tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(user_controller.router, prefix="/api/users", tags=["users"])
app.include_router(project_controller.router, prefix="/api/projects", tags=["projects"])
app.include_router(user_project_role_controller.router, prefix="/api/user_project_roles", tags=["user_project_roles"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}