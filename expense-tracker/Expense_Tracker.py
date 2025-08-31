import numpy as np
import shutil as sh
import os 

def chk_file(): # Function to check if the file exists, if not create it
    if not os.path.exists("ExpenseTracker.txt"):
        with open("ExpenseTracker.txt", "w") as file:
            file.write("") # Creates an empty file

text_1 = "Expense Tracker v1.0" # Opening menu and welcome message
width = sh.get_terminal_size().columns
width1= width//2
border = "=" * width1
print(border)
print(text_1.center(width1))
print(border) 
print("Welcome to the Expense Tracker!")
print("You can add, view, and delete your expenses and income.")
print("Your history will be saved in a file named 'ExpenseTracker.txt'.")   
print(border)
user_inp_1 = str(input("Type 'start' to begin or 'exit' to quit: ")).lower()

def exp_inc(): # Function to add expense/income
    print(border)
    print("Add Expense/Income".center(width1))
    print(border)
    user_inp_3 = str(input("Type 'expense' to add an expense or 'income' to add income: ")).lower()
    if user_inp_3 == "expense":
        try:
            amount = float(input("Enter the expense amount: "))
            description = input("Enter a description for the expense: ")
            with open("ExpenseTracker.txt", "a") as file:
                file.write(f"Expense: {amount}, Description: {description}\n")
            print(f"Expense of {amount} added successfully.")
            print(f"Description of the expense: {description}")
            print(f"Expense recorded in 'ExpenseTracker.txt'. Kindly check the file for details.")
            print(f"Reverting to main menu...")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            exp_inc()
    elif user_inp_3 == "income":
        try:
            amount = float(input("Enter the income amount: "))
            description = input("Enter a description for the income: ")
            with open("ExpenseTracker.txt", "a") as file:
                file.write(f"Income: {amount}, Description: {description}\n")
            print(f"Income of {amount} added successfully.")
            print(f"Description of the income: {description}")
            print(f"Income recorded in 'ExpenseTracker.txt'. Kindly check the file for details.")
            print(f"Reverting to main menu...")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            exp_inc()
    else:
        print("Invalid input. Please type 'expense' or 'income'.")
        exp_inc()
    main_menu() # Return to main menu after adding expense/income

def v_exp_inc(): # Function to view expenses/income
    print(border)
    print("View Expenses/Income".center(width1))
    print(border)
    chk_file() # Ensure the file exists before trying to read it
    try:
        with open("ExpenseTracker.txt", "r") as file:
            content = file.readlines()
            if not content:
                print("No expenses or income recorded yet.")
            else:
                print("Here are your recorded expenses and income:")
                for line in content:
                    print(line.strip())
                p=input("Press Enter to return to the main menu...")
        print(f"Reverting to main menu...")
        main_menu() # Return to main menu after viewing expenses/income    
    except FileNotFoundError:
        print("No records found. Please add some expenses or income first.")
        print(f"Reverting to main menu...")
        main_menu() # Return to main menu after viewing expenses/income

def del_exp_inc(): # Function to delete expense/income 
    print(border)
    print("Delete Expense/Income".center(width1))   
    print(border)
    chk_file() # Ensure the file exists before trying to read it
    try:
        with open("ExpenseTracker.txt", "r") as file:
            content = file.readlines()
            if not content:
                print("No expenses or income recorded yet.")
                print(f"Reverting to main menu...")
                main_menu() # Return to main menu if no records exist
            else:
                print("Here are your recorded expenses and income:")
                for idx, line in enumerate(content, start=1):
                    print(f"{idx}. {line.strip()}")
                try:
                    del_idx = int(input("Enter the number of the entry you want to delete (or 0 to cancel): "))
                    if del_idx == 0:
                        print("Deletion cancelled. Reverting to main menu...")
                        main_menu() # Return to main menu if deletion is cancelled
                    elif 1 <= del_idx <= len(content):
                        removed_entry = content.pop(del_idx - 1)
                        with open("ExpenseTracker.txt", "w") as file:
                            file.writelines(content)
                        print(f"Deleted entry: {removed_entry.strip()}")
                        print(f"Reverting to main menu...")
                        main_menu() # Return to main menu after deletion
                    else:
                        print("Invalid number. Please try again.")
                        del_exp_inc() # Retry deletion if invalid number
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
                    del_exp_inc() # Retry deletion if invalid input
    except FileNotFoundError:
        print("No records found. Please add some expenses or income first.")
        print(f"Reverting to main menu...")
        main_menu() # Return to main menu if file not found

def main_menu(): # Main menu function
    print(border)
    print("Main Menu".center(width1))
    print(border)
    print("1. Add Expense/Income")
    print("2. View Expenses/Income")
    print("3. Delete Expense/Income")
    print("4. Exit")
    print(border)
    user_inp_2 = str(input("Please select an option (1-4): ")) # Getting user input for main menu options
    if user_inp_2 == "1":
        print("You selected to add an expense/income.")
        exp_inc()
        # function for adding expense/income functionality
    elif user_inp_2 == "2":
        print("You selected to view expenses/income.")
        v_exp_inc()
        # function for viewing expenses/income functionality
    elif user_inp_2 == "3":
        print("You selected to delete an expense/income.")
        del_exp_inc()
        # function for deleting expense/income functionality
    elif user_inp_2 == "4":
        chk_file() # Ensure the file exists before exiting
        print("Logs are saved in 'ExpenseTracker.txt'.")
         # function for exiting the tracker
        print("Exiting the Expense Tracker...")
        exit()
    else:
        print("Invalid input. Please select a valid option (1-4),",f"you entered: {user_inp_2}")
        main_menu()       

if user_inp_1 == "start": # Processing user input to start or exit the tracker
    print("Great! Let's get your expenses and income sorted.")
    main_menu()

elif user_inp_1 == "exit":
    print("Thank you for using the Expense Tracker.")
    exit()
else:
    print("Invalid input. Please restart the program and type 'start' or 'exit' only.",f" You entered: {user_inp_1}")
    exit()

