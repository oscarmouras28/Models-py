import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    ID = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), primary_key=True, nullable=False)
    Followers = relationship('Follower', backref='user', lazy=True)

class Follower(Base):
    __tablename__='Follower' 
    user_from_id = Column(Integer, ForeignKey('User.ID'), primary_key=True)   
    user_to_id = Column(Integer, ForeignKey('User.ID'))
    Followers = relationship('Follower', backref='user', lazy=True)  
    
    
class Comment(Base):
    __tablename__='Comment'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id= Column(Integer, ForeignKey('User.ID')) 
    post_id= Column(Integer, ForeignKey('Post.ID')) 

class Post(Base):
    __tablename__='Post'
    ID = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('User.ID')) 

class MediaTypes(enum.Enum):
    IMAGE = "image"
    VIDEO = "video"

class Media(Base):
    __tablename__='Media'
    ID = Column(Integer, primary_key=True)
    tipo = Column(Enum(MediaTypes), nullable=False)
    url = Column(String(250), nullable=False)
    post_id= Column(Integer, ForeignKey('Post.ID')) 
    
    
    
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e