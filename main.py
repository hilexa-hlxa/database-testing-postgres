from fastapi import FastAPI, Depends, HTTPException
import services, models, schemas
from db import get_db, engine
from sqlalchemy.orm import Session
import asyncio
import uvicorn

app = FastAPI()

@app.get("/")
def testing():
    return {"ok": True}


@app.get("/user", response_model=list[schemas.User])
async def get_all_users(db: Session = Depends(get_db)):
    return services.get_user(db)

@app.get("/users/{id}", response_model=schemas.User)
def get_user_byid(id: int, db: Session = Depends(get_db)):
    user_queryset = services.get_user_byid(db, id)
    if user_queryset:
        return user_queryset
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users/", response_model=schemas.User)
def create_new_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create_user(db, user)

@app.put("/users/{id}", response_model=schemas.User)
def update_user_byid(user: schemas.UserCreate, user_id: int, db: Session = Depends(get_db)):
    db_update = services.update_user(db, user, user_id)
    if not db_update:
        raise HTTPException(status_code=404, detail="User not found")
    return db_update

@app.delete("/users/{id}", response_model=schemas.User)
def delete_user_byid(user_id: int, db: Session = Depends(get_db)):
    user_delete = services.delete_user(db, user_id)
    if user_delete:
        return user_delete
    raise HTTPException(status_code=404, detail="User not found")




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)