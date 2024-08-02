from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from models.role import Role
from models.project import Project
from models.user_project_role import UserProjectRole
from typing import List
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    # Implement your token decoding and user fetching logic here
    user = db.query(User).filter(User.username == token).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    return user

def has_project_role(project_id: int, required_roles: List[str]):
    def dependency(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
        project = db.query(Project).filter(Project.id == project_id).first()
        if not project:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
        
        user_roles = db.query(Role).join(UserProjectRole).filter(
            UserProjectRole.user_id == current_user.id,
            UserProjectRole.project_id == project.id
        ).all()
        
        user_role_names = [role.name for role in user_roles]
        if not any(role in user_role_names for role in required_roles):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied")
        
        return current_user
    return dependency
