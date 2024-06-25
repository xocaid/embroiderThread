# Helper Functions
def user_input_int():
    while True:
        user_input = input('Enter a number.')

    ## Can delete once done - only for debugging purposes
        print(user_input)

        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print("Try again, enter a number.")