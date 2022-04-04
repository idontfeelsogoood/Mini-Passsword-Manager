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
    new_user_id = amount_of_users()                             # id
    new_user = db.User(new_user_id,new_login,new_password)      # passing arguments to 'User' Class from db.py
    session.add(new_user)                                          # adding user to database
    session.commit()

def clear_database():
    session.query(db.User).delete()                 #Special function do delete all records from database 
    session.commit()



