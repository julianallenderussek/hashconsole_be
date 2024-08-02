from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user_project_role_schema import UserProjectRoleCreate, UserProjectRole
from app.models.user_project_role import UserProjectRole as UserProjectRoleModel
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=UserProjectRole, status_code=status.HTTP_201_CREATED)
async def assign_role(user_project_role: UserProjectRoleCreate, db: Session = Depends(get_db)):
    db_user_project_role = UserProjectRoleModel(
        user_id=user_project_role.user_id,
        project_id=user_project_role.project_id,
        role_id=user_project_role.role_id
    )
    db.add(db_user_project_role)
    db.commit()
    db.refresh(db_user_project_role)
    return db_user_project_role

@router.get("/{user_project_role_id}", response_model=UserProjectRole)
async def get_user_project_role(user_project_role_id: int, db: Session = Depends(get_db)):
    user_project_role = db.query(UserProjectRoleModel).filter(UserProjectRoleModel.id == user_project_role_id).first()
    if user_project_role is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="UserProjectRole not found")
    return user_project_role
