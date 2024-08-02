from pydantic import BaseModel

class UserProjectRoleBase(BaseModel):
    user_id: int
    project_id: int
    role_id: int

class UserProjectRoleCreate(UserProjectRoleBase):
    pass

class UserProjectRole(UserProjectRoleBase):
    id: int

    class Config:
        orm_mode = True
