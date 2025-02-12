"""
This part of the program actually handles all the to-do list functionality.
This program will only call the actions in the necessary order. 
"""
import task_actions as action
import text_content as content

def main(username):
    #Let's load everything that is in the previous file 
    #This makes the user more smoother 
    #However remember to save the data in the end when the user ends the program.
    file_data = action.get_file_data(username)
    
    #prompt if the user wants to see their past progress
    yn = action.get_yesorno("Would you like to see what you had in your file before moving forward? (Y/N)")
    if yn:
        action.display_tasks(file_data)
    
    #loop over the menu options 
    #only break out of loop when the user quits the program
    print(content.get_divider())
    
    print("Welcome to the workstation!\nHere is the menu: ")
    while True:
        
        #returns a number correlating to the action the user chose from the menu
        action_num = action.menu()
        
        #sort based on the choice for main menu
        if action_num == 0: #end program
            print(content.get_divider("large"))
            return file_data
        
        elif action_num == 1: #Show the submenu for view
            
            #get the choice for the submenu
            sub_action_num = action.menu("view")
            
            if sub_action_num == 1: #View incomplete tasks
                action.display_sorted_tasks(file_data, "incomplete")
            elif sub_action_num == 2: #View complete tasks
                action.display_sorted_tasks(file_data, "completed")
            elif sub_action_num == 3: #view all tasks
                action.display_sorted_tasks(file_data)
            else: #0 or another number: the loops runs again i.e. goes back to main menu
                pass           
            
        elif action_num == 2: #Show the submenu for edit
            
            #get the choice for the submenu
            sub_action_num = action.menu("edit")
            
            #prompt the user to see if they would like to see the list of tasks before editing
            yn = action.get_yesorno("Would you like to view all the tasks before selecting one to edit? (Y/N)")
            if yn:
                action.display_tasks(file_data)
            
            #prompt the user to choose which task they would like to edit
            edit_location = input("Please enter which task you would like to edit:\n(You can either write the whole task or write down the number of the task you want to edit when listing the whole document.")
            
            #find the index of the task the user wants to edit
            edit_index = action.user_choice(edit_location, file_data)
            
            if sub_action_num == 1: #Edit a task name
                while True: #looping to make sure the user can confirm the change they want to make
                    #prompt the user to enter the new task name
                    new_taskname = input("Please enter what you want the new task name to be: ")
                    
                    #double checking the new task name
                    print(f"You entered '{new_taskname}'.")
                    yn = action.get_yesorno("Is that the desired change in task name? (Y/N) ")
                    if yn:
                        #Dual confirmation done, change the task name and break out of the loop
                        file_data[edit_index]["task"] = new_taskname
                        break
                    else:                    
                        print("Let's try again and get the name right!")
                      
            elif sub_action_num == 2: #Edit the status of a task
                while True: #looping to give the user a change to confirm the changes
                    #promt user for the new status
                    new_status = input("Please enter what you want the new status to be: ")
                    
                    #Giving the user a chance to double check the changes
                    print(f"You entered {new_status}.")
                    yn = action.get_yesorno("Is that the desired new status? (Y/N)")
                    if yn:
                        #Double confirmation done, change the status and exit the loop
                        file_data[edit_index]["status"] = new_status
                        break
                    else:
                        print("Let's try again and get the status right!")
                    
            elif sub_action_num == 3: #Edit the priority of a task
                print("The priority values go from 1, being the most important, to 3, being the least important.")
                while True: #looping for confirmation
                    new_priority = action.get_int("Please enter the new priority number for the chosen task: ", "Please choose one of the three options.", 4)
                    if new_priority == 0: #easter egg basically
                        print("Alright, you caught a bug that I was too lazy to fix.\nGo on and gloat but please choose within the acceptables values okay?")
                    else: #letting the user confirm changes
                        print(f"You entered {new_priority}")
                        yn = action.get_yesorno("Is that the desired new priority number? (Y/N)")
                        if yn:
                            file_data[edit_index]["prioritylevel"] = new_priority
                            break
                        else:
                            print("Let's try that again shall we?")                
            
            else: #0 or another number: the loops runs again i.e. goes back to main menu
                pass 
            
        elif action_num == 3: #Show the submenu for delete
            
            #get the choice for the submenu
            sub_action_num = action.menu("delete")
            
            if sub_action_num == 1: #Delete a task
                
                #prompt the user to see if they would like to see the list of tasks before deleting
                yn = action.get_yesorno("Would you like to view all the tasks before selecting one to delete? (Y/N)")
                if yn:
                    action.display_tasks(file_data)
            
                #prompt the user to choose which task they would like to delete
                delete_location = input("Please enter which task you would like to delete:\n(You can either write the whole task or write down the number of the task you want to delete when listing the whole document.")
                
                #find the index of the task the user wants to delete
                edit_index = action.user_choice(delete_location, file_data)
                
                del file_data[edit_index] #deleting the index                  
                
            elif sub_action_num == 2: #Delete all tasks
                
                file_data.clear()
            
            else: #0 or another number: the loops runs again i.e. goes back to main menu
                pass
            
        elif action_num == 4: #Add a new task
            while True: #so that the user can confirm the task name
                #prompt to add a new task    
                taskname = input("Please enter task that you want to add to the list: ")
                
                #confirm the name for the task
                print("You entered '{taskname}'.")
                yn = action.get_yesorno("Do you confirm the name of the task?(Y/N) ")
                if yn: #user confirmation, add the task to the list
                    file_data.append({"task":taskname, "status":"Just started", "prioritylevel":"3"})
                    break
                else:
                    print("Let's try new name for the task.")
        
        elif action_num == 5: #Mark the selected task as complete
            #prompt the user to see if they would like to see the list of tasks before editing
            yn = action.get_yesorno("Would you like to view all the tasks before selecting one to edit? (Y/N)")
            if yn:
                action.display_tasks(file_data)    
            
            while True:                                
                #prompt the user to choose which task they would like to mark completed
                completed_location = input("Please enter which task you would like to mark completed:\n(You can either write the whole task or write down the number of the task you want to mark completed when listing the whole document.")
                
                #find the index of the task the user wants to mark completed
                complete_index = action.user_choice(completed_location, file_data)
                
                print(f'The task you want to mark as completed is {file_data[complete_index]["task"]}.')
                yn = action.get_yesorno("Is that the right task to be marked completed? (Y/N)")
                if yn:
                    file_data[complete_index]["status"] = "Completed"
                    break
                else:
                    print("Let's try that again.")
        
        print(content.get_divider())

if __name__ == "__main__":
    main()
    
    
    
    
    