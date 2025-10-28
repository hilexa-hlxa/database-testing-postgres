from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    surname: str
    bio: str
    age: int

class UserCreate(UserBase):
    pass

class User(UserBase):
    id : int

    class config:
        orm_mode = True # if pydantic <2.x
        # from_attribute = True # else if pydantic >2.x