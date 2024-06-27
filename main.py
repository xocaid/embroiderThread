from menus.brands.manage_brands_menu import manage_brands_menu
from menus.threads.manage_threads_menu import manage_threads_menu
from menus.utilities import user_input_int

def main():
    print('What action do you want to perform?')

    print('1. Manage Brands')
    print('2. Manage Threads')

    user_input = user_input_int(2)

    if user_input == 1:
        manage_brands_menu()
    elif user_input == 2:
        manage_threads_menu()
    else:
        print('See you next time.')

main()
