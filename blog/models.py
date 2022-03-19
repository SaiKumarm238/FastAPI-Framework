from operator import index
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique =True)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    creator = relationship("User", back_populates="blog")
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique =True)
    email = Column(String, unique =True)
    password = Column(String)
    
    blog = relationship("Blog", back_populates="creator")