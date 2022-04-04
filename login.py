import string
from tokenize import String
import db
from db import *
from sqlalchemy.orm import sessionmaker
import random




#new session
Session = sessionmaker(bind=db.engine)
session = Session()


#Login function
def login_user(login,password):
    for i in session.query(db.User).filter(db.User.user_login == login):    
        if(i.user_password == password):                                    
            return True
        else:
            return False

    return False

