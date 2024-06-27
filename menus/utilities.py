# Helper Functions
def user_input_int(maxNum):
    while True:
        user_input = input('Enter a number.')

    ## Can delete once done - only for debugging purposes
        print(str(user_input) + 'user_input_int() --> utilities.py')

        try:
            user_input = int(user_input)
            if user_input > maxNum or user_input <=0:
                raise ValueError
            return user_input
        except ValueError:
            print("Try again, enter a number.")

def user_input_option(valid_options, maxNum):
    while True:
        user_input = input('Enter your selection.')

    ## Can delete once done - only for debugging purposes
        print(user_input)
        print('Printing from user_input_option --> utilities.py')

        try:
            user_input = int(user_input)
            if user_input > maxNum or user_input <=0:
                raise ValueError
            return user_input
        except ValueError:
            if user_input.upper() in valid_options:
                return user_input.upper()
            
            print("Try again, enter a valid selection.")