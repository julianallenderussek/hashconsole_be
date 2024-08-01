from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from sqlalchemy import text
from config.db import engine, SessionLocal
from sqlalchemy.orm import Session
from helpers.dbhelpers import serializeResults, serializeResult

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

# This is to validate incoming requests
class PostBase(BaseModel):
  title: str
  content: str
  user_id: int

class UserBase(BaseModel):
  username: str
  
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# best way to make api
@app.post('/api/users', status_code=status.HTTP_201_CREATED)
async def post_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # Refresh to get the auto-generated ID
    return {"id": db_user.id}

# best way to make api
@app.get('/api/users/{user_id}', status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: db_dependency):
    query = text("SELECT * FROM users WHERE id = :id LIMIT 1")
    result = db.execute(query, {'id': user_id}).fetchone()     
    print(result)
    if result:
        user = serializeResult(models.User, result)
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

@app.get('/api/users', status_code=status.HTTP_200_OK)
async def list_users(db: db_dependency):
    query = text("SELECT id, username FROM users")
    results = db.execute(query).fetchall()
    users = serializeResults(models.User, results) 
    return users