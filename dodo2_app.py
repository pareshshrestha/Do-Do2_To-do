"""
This is Dodo 2.0. 
It is still a text based to-do program. 
There shall be additional features regarding saving files and being more decentralized. 

Future development:
    1. Make the user sign in using a password.
"""
import text_content as content 
import task_actions as action
import user_login as login 
import todo
import sys

def main():
    #Start of the Dodo2
    
    #Checking and assigning the username if called with the application
    #Else, it just returns "User"
    user_name = action.get_user_name(sys.argv)
    
    #This calls a file that manages to do 3 things:
    #1. Gets the user's full name.
    #2. Adds security as only the correct full name and password will allow you to edit or view the file again. Controlled by boolean value of attempt.
    firstname, middlename, lastname, attempt = login.login(user_name)
    fullname = firstname + middlename + lastname
    
    #Place holder for future application where we attempt to secure the to-do list. 
    #If the attempt value is False, the program will just exit and end
    if attempt == False:
        sys.exit()
    
    print(content.get_divider())
        
    #start the actual program
    task_list = todo.main(fullname)
    
    #asks the user if they want to save the data or not
    #also displays a small summary of the user's actions
    login.logout(fullname, task_list)    
    

if __name__ == "__main__":
    main()