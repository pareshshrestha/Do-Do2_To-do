"""
This file holds all actions that can be called for Dodo2.
"""
from pathlib import Path
import csv
import tabulate
import text_content as content

#This function checks if a certain file exists or not.
#Returns boolean, True if file exists and False if it does not. 
def file_exists(filename):
    filename = filename.lower() #because all file names are stored in lowercase
    file = Path(filename+'.csv')
    if file.exists():
        return True
    else:
        return False

#This function checks if the user passes their name while calling the Dodo application.
#This is just to make the application feel more personal right from the start.
def get_user_name(user_input):
    if len(user_input) > 1:
        return user_input[1].strip().capitalize()
    else:
        return "User"

#This function prompts to list their whole name. 
#This function then returns first name, first middle name and last name.
def get_full_name(name):
    print(f"First, let's confirm your full name {name}.")
    fullname = input("Please enter your full name: ").split()
    if len(fullname) == 2:
        return fullname[0], "", fullname[-1]
    else:
        return fullname[0], fullname[1], fullname[-1]

#This function creates a csv file according to the passed filename.
#This function also formats the csv file to be ready to used by Do-do with the right header for the columns.
def create_csv_file(filename):
    with open(filename+".csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=content.get_column_titles().keys())
        writer.writeheader()  # Write column titles as header

#Reads the file with the name passed in the fucntion.
#Returns a list of dictionaries
def get_file_data(filename):
    tasks = []
    with open(filename+".csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            tasks.append(row)
    return tasks
    
#Prompts the user to say yes or no
#Returns true if yes and False if no
def get_yesorno(prompt):
    while True:
        user_input = input(prompt).strip().upper()
        
        if user_input == "Y" or user_input == "YES":
            return True
        elif user_input == "N" or user_input == "NO":
            return False
        else:
            print("Please type Y for yes or N for no.")
            
#Takes a list of dictionaries and turns it into a table
def display_tasks(task_list):
    if len(task_list) < 1:
        print("You currently have no tasks.")
    else:
        # Generate custom index starting from 1
        index = [i + 1 for i in range(len(task_list))]
        print(tabulate.tabulate(task_list, headers= "keys", showindex=index))

#only accepts integers within the range and returns it
def get_int(prompt, error_message, valid_range):
    while True:
        try:
            num = int(input(prompt))
            if num >= 0 and num < valid_range:
                return num
            else: 
                print(f"Please enter an integer between 0 and {valid_range-1}. ")
        except ValueError:
            print(error_message)
                
     
#Displays the menu and returns the number correlating with the action the user wants to perform
def menu(type = "main"):    
    #test for which part of menu to print
    #gets the main menu
    if type == "main":
        menulist = content.get_menu()
    #gets the sub-menu of view
    elif type == "view":
        menulist = content.get_menu_view()
    #gets the sub-menu of edit
    elif type == "edit":
        menulist = content.get_menu_edit()
    #gets the sub-menu of delete
    elif type == "delete":
        menulist = content.get_menu_delete()        
    
    #print the actual menu
    print(content.get_divider())
    for i in range(len(menulist)):
        print(i, menulist[i], sep=". ")
    print(content.get_divider())
    #return menu selection
    user_action = get_int("Type the number of the menu option you choose: ", "Please choose a menu option number. ", len(menulist))
    return user_action

#sorts list of dictionaries as completed and incomplete lists of dictionaries
def sort_tasks(task_list):
    incomplete = []
    completed = []    
    for row in task_list:
        if row["status"] == "Completed":
            completed.append(row)
        else:
            incomplete.append(row)    
    return incomplete, completed    

#sorts the tasks according to their status and displays either complete or incomplete ones
def display_sorted_tasks(task_list, status = None):
    incomplete, completed = sort_tasks(task_list)    
    if status == "incomplete":
        display_tasks(incomplete)
    elif status == "completed":
        display_tasks(completed)
    else:
        display_tasks(incomplete)
        print(content.get_divider("large"))
        display_tasks(completed)

#Determine if the user has entered integer or string 
#If integer, return the integer value
#If string, search for the row number of the string input
def user_choice(userinput, tasklist):
    try:
        #test if it is a number or not
        index = int(userinput)
        
        #returns the number if it is a valid input 
        if 0 < index <= len(tasklist):
            return index - 1
        else: #lets get teh index 
            while True:
                num = get_int("The number you have entered does not fall within the task list.\nPlease enter within the range: ", "Please enter an integer value within the range", len(tasklist))
                if 0 < num <= len(tasklist):
                    return num-1 
                
    except ValueError: #incase the input is all string
        while True:
            #checking for the task index for the entered task 
            for i in range(len(tasklist)):
                task_inlist = tasklist[i]["task"]
                if task_inlist.strip().upper() == userinput.strip().upper():
                    return i
            userinput = input("The task you entered does not exist. (Hint spaces between words can cause this issue)\nTry typing the task name again.")

#writes the file data passed in tasks into the file "name"
def save_file(name,tasks):
    with open(name+".csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=content.get_column_titles().keys())
        writer.writeheader()  # Write column titles as header
        writer.writerows(tasks) #writes the tasks into the file name
        
    