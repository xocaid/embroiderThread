from menus.brands.manage_brands_menu import manage_brands_menu
from menus.threads.manage_threads_menu import manage_threads_menu
from menus.utilities import user_input_int
import sys

def main():
    print('What action do you want to perform?')

    print('1. Manage Brands')
    print('2. Manage Threads')
    print('3. Would you like to exit the program?')

    user_input = user_input_int(3)

    if user_input == 1:
        manage_brands_menu()
    elif user_input == 2:
        manage_threads_menu()
    else:
        print('You are exiting the program.')
        print('See you next time!')
        sys.exit(0)

main()