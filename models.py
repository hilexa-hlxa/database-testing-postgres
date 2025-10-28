from db import Base
from sqlalchemy import Integer, Column, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    bio = Column(String, index=True)
    age = Column(Integer)
