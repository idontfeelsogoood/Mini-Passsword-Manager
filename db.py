import string
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#######################################################################
#The most important .py in which we establish connection with database#
#######################################################################



#Connect with database
#Database name = 'sqlalchemy.sqlite'

engine = create_engine('sqlite:///sqlalchemy.sqlite',echo=True)

#Base declaration
base = declarative_base()


class User (base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)             #Creating table structure
    user_login = Column(String)
    user_password = Column(String)
    
    def __init__(self,user_id,user_login,user_password):
        self.user_id = user_id                                  #Constructor need to pass arguments for new user instanlty to class
        self.user_login = user_login
        self.user_password = user_password


base.metadata.create_all(engine)                #CREATE DATABASE 'smthing like commit()'


