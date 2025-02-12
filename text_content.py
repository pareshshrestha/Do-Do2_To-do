'''
This python file will return all the important text content for the to-do list. 
This will save files ranging from opening statements, menu list and program end. 
The programs here will not print but only return strings. 
'''

#This fucntion returns a greeting to the user. 
#The message is addressed to either User or sys.argv input when calling Dodo2
def get_opening_msg(name):
    return f"""Welcome to Dodo 2.0!
Your everyday text-based to-do list.
Hello {name}! Let's get started.
"""

#This funciton returns a Dictionary with column names as keys
def get_column_titles():
    return {
        "task": "", 
        "status": "", 
        "prioritylevel": ""
    }  

# Returns the keys for the dictionary
def get_keys():
    return ["task","status","prioritylevel"]  
    
 #returns a divider according to prompt   
def get_divider(size = "small"):
    if size == "small":
        return "\n" +("-" * 30)+ "\n"
    elif size == "large":
        return "\n"+("#-" * 20)+"\n"

#returns the list of main menu options
def get_menu():
    return [
        "Exit the program",
        "View tasks",
        "Edit tasks",
        "Delete tasks",
        "Add task",
        "Mark task complete"        
    ]

#returns the list of view submenu options
def get_menu_view():
    return [
        "Go back",
        "View incomplete tasks",
        "View complete tasks",
        "View all"
    ]

#returns the list of edit submenu options
def get_menu_edit():
    return [
        "Go back",
        "Edit a task",
        "Edit the status of a task",
        "Edit the priority level of a task"
    ]

#returns the list of delete submenu options
def get_menu_delete():
    return [
        "Go back",
        "Delete a task",
        "Delete all"
    ]





