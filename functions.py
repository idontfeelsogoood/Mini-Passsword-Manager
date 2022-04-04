from genericpath import exists
import string
import time
import os.path

from regitser_user import amount_of_users




#Python file which contains 'Add new Password' && 'Show your password (login required)' functions

#Menu
def show_menu():
    print()
    print("(1) Add new Password")
    print("(2) Show your password (login required)")         
    print("(3) Create User")
    print("(4) Clear User Database (Watch out)")
    print("(5) Exit")

#Animation if user enter wrong input
def waiting_processing_dot():
    processing = "Processing"
    print()

    for i in range(4):
        time.sleep(0.2)
        print(processing+i*".")                         
    time.sleep(1)

    print()


#check if .txt file exist if not create one
def check_file_exist():                                     
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
            #Checking if .txt file is empty         
            first_char = file.read(1)      

            #counting lines in .txt file 
            if(first_char):                                        
                for count , line in enumerate(file):                     
                    pass
                lines = count+2

            #if .txt file is empty lines=1
            else:
                count = 1
                lines = count               
        
        finally:
            file.close()


    #expression which is passed to .txt file 
    password_id = "("+str(lines)+") "                                                                      
    password_expression = password_id+"Password Information: ",password_theme,"  Password:",new_password,"\n" 
    password_expression = " ".join(password_expression)                 
    
    #Adding expression to .txt file 
    with open("passwords.txt","a") as file:
        try:
            file.write(str(password_expression))                
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
            
               




        
