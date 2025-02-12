"""
This file is to log-in the user.
Currently, it only checks if the user has a file with us or not. 
If not, it creates a file with the user's name. 
In the future, this will check if the user knows the password for the csv file to make sure-
that only the correct user can view and edit their to-do list. 
"""

import task_actions as action
import text_content as content 

def login(username):
    
    #Welcomes the user with their name or just as User
    print(content.get_opening_msg(username))
    
    #Get the user's full name
    first_name, middle_name, last_name = action.get_full_name(username)
    file_name = first_name + middle_name + last_name
    
    #Checking if a file on the user exists
    #If there is no previos file, make a new file
    if action.file_exists(file_name):
        print(f"Welcome back {first_name}. We already have a file on you!\n")
    else: 
        print(f"We do not have a file on you {first_name}. Let's make a new one for you.\nWelcome to the Do-do To-do family!")
        #create a file according to the file name passed with the correct format for to-do list
        action.create_csv_file(file_name) 
    
    #This is a placeholder for future login security application
    login_attempt_success = True;
        
    return first_name, middle_name, last_name, login_attempt_success

def logout(username, tasklist):
    
    #ask the user if they want to save the new data or not 
    #if true, save the data in the given username 
    save_file = action.get_yesorno("Would you like to save the file?(Y/N) ")
    if save_file: #save the file
        action.save_file(username, tasklist)
    
    incomp, comp = action.sort_tasks(tasklist)
    print(f"Short summary:\nYou have {len(incomp)} tasks left to finish.\nYou finished {len(comp)} tasks. Good job.\nThank you for using Dodo2.")
    print(content.get_divider("large"))
    
    
    
    
    
    
    