from menus.brands_menu import brands_menu
from menus.threads_menu import threads_menu
from menus.utilities import user_input_int

def main():
    print('What action do you want to perform?\n')

    print('1. Manage Brands\n')
    print('2. Manage Threads\n')

    user_input = user_input_int()

    if user_input == 1:
        brands_menu()
    elif user_input == 2:
        threads_menu()
    else:
        print('See you next time.')

main()
