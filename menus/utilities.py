## Helper Functions
import sys

## Requests NUMERICAL user input. 
# maxNum is the max/last number displayed on the list; numbers not on the list will not exist and may cause error
def user_input_int(maxNum):
    while True:
        user_input = input('Enter a number.')

    ## Can delete once done - only for debugging purposes
        print('1Printing from utilities.py --> user_input_int(). User input: ' + str(user_input) )

        try:
            user_input = int(user_input)
            if user_input > maxNum or user_input <=0:
                raise ValueError
            return user_input
        except ValueError:
            print("Try again, enter a number.")

## Requests NUMERICAL & ALPHABETICAL user input. 
# maxNum is the max/last number displayed on the list; numbers not on the list will not exist and may cause error
# valid_options --> represents only the valid letter(s).
def user_input_numalp(valid_options, maxNum):
    while True:
        user_input = input('Enter your selection.')

    ## Can delete once done - only for debugging purposes
        print('2Printing from utilities.py  --> user_input_option. User input: '+ str(user_input))

        try:
            user_input = int(user_input)
            if user_input > maxNum or user_input <=0:
                raise ValueError
            return user_input
        except ValueError:
            if user_input.upper() in valid_options:
                return user_input.upper()
            
            print("Try again, enter a valid selection.")

## Request user input to: view current/previous menu or exit the program.
def which_menu(curr_menu_fxn, prev_menu_fxn,curr_menu_name, prev_menu_name):
    print('What would you like to do?')

    print(f'1. View the {curr_menu_name} menu?')
    print(f'2. Go back to the {prev_menu_name} menu?')
    print('3. Exit the program.')

    user_input = user_input_int(3)

    if user_input == 1: 
        print("From Utilities: Line 70")
        curr_menu_fxn()
        print("From Utilities: Line 72")
    elif user_input == 2:
        print("From Utilities: Line 74")
        prev_menu_fxn()
        print("From Utilities: Line 76")
    else:
        print('You are exiting the program.')
        print('See you next time!')
        sys.exit(0)
     
    which_menu(curr_menu_fxn, prev_menu_fxn, curr_menu_name, prev_menu_name)

## Menu List Array
def crud_ops(cat):
    crud_questions = [
        f'List {cat}',
        f'Create New {cat}',
        f'Edit {cat}',
        f'Delete {cat}'
    ]
    return crud_questions

# List CRUD operations
def loop_crud_ops(x):
    for i in range(0, len(x)):
        print(i+1,'.', x[i])