from genericpath import exists
import string
import time
import os.path

from regitser_user import amount_of_users




#Python file which contains 'Add new Password' && 'Show your password (login required)' functions


def show_menu():
    print()
    print("(1) Add new Password")
    print("(2) Show your password (login required)")         #Menu
    print("(3) Create User")
    print("(4) Clear User Database (Watch out)")
    print("(5) Exit")


def waiting_processing_dot():
    processing = "Processing"
    print()

    for i in range(4):
        time.sleep(0.2)
        print(processing+i*".")                         #Animation if user enter wrong input
    time.sleep(1)

    print()



def check_file_exist():                                     #check if .txt file exist if not create one
    file_exist = exists("passwords.txt")
    if(file_exist):                                                 
        return True
    else:
        with open("passwords.txt","w") as f:
            f.close()

    
# Adding new Password to .txt file
def adding_New_Password(password_theme:string,new_password:string):

    check_file_exist()                                                      
    with open("passwords.txt","r") as file:
        try:
            first_char = file.read(1)           #Checking if .txt file is empty            

            if(first_char):                                        
                for count , line in enumerate(file):                    #counting lines in .txt file  
                    pass
                lines = count+2

            else:
                count = 1
                lines = count               #if .txt file is empty lines=1
        
        finally:
            file.close()
    
    password_id = "("+str(lines)+") "                                                                      
    password_expression = password_id+"Password Information: ",password_theme,"  Password:",new_password,"\n" 
    password_expression = " ".join(password_expression)                 #expression which is passed to .txt file 
    

    with open("passwords.txt","a") as file:
        try:
            file.write(str(password_expression))                #Adding expression to .txt file 
        finally:
            file.close()



#Showing all records
def showing_passwords():
    showing_file_exist = exists("passwords.txt")

    if(showing_file_exist):                                     

        with open("passwords.txt") as f:
            linestable = f.readlines()
            for line in linestable:
                print(line)
            
               




        
