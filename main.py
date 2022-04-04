from itertools import count
from re import S
from functions import *
import time
import os

from regitser_user import *
from db import *
from login import *


main_menu_Flag = True


print("Welcome to PasswordManager !!!") 

while main_menu_Flag:
    
    show_menu()
    
    try:
        user_choice = int(input("Option: "))                #User choice 

    except ValueError:
        time.sleep(1)
        waiting_processing_dot()                                #Exception if user type wrong input 'fancy dot'

        print("You must Input Integer")
        user_choice = 0
        
    #Add Password to .txt file
    if user_choice == 1:
        print()
        password_theme = input("Input informations about your password: ")                  
        user_password = input("Enter your Password: ")
        adding_New_Password(password_theme,user_password)

    #Show passwords
    elif user_choice == 2:
        logged = False

        checking_user_login = str(input("Login: "))
        checking_user_password = str(input("Password: "))                           #loggin
        if(login_user(checking_user_login,checking_user_password)):

            print("\nLogin Sucessfull\n")
            logged = True
        else:
            print("\nWrong login or password \n")
            logged= False
        
        if(logged):
            print("\nShowing Your Passwords \n")
            showing_passwords()
        


    #Creating new user
    elif user_choice == 3:
        print("\nCreating...\n")
        creating_new_user_login = str(input("Login: "))
        creating_new_user_password = str(input("Password: "))
        creating_user(creating_new_user_login,creating_new_user_password)       #function to create new user
        
    elif user_choice == 4:
        clear_database()      #Special function to delete all database records

    
    elif user_choice == 5:                                                  #EXIT
        main_menu_Flag = False
    
    