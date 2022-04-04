import string
from tokenize import String
import db
from sqlalchemy.orm import sessionmaker
import random


#Creating new session
Session = sessionmaker(bind=db.engine)
session = Session()

#Checking how many users are in database to set id for new user
def amount_of_users():
    amount_of_users = 0
    for i in session.query(db.User).all():
        amount_of_users += 1

    return amount_of_users
        
#Creating new user
def creating_user(new_login,new_password):
    new_user_id = amount_of_users()                             
    new_user = db.User(new_user_id,new_login,new_password)      
    session.add(new_user)                                          
    session.commit()
    
#Special function do delete all records from database 
def clear_database():
    session.query(db.User).delete()                 
    session.commit()



