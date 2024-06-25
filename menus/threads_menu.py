from menus.utilities import user_input_int
from menus.list_thread_menu import list_thread_menu
from menus.create_thread import create_thread_menu
from menus.edit_thread import edit_thread
from menus.delete_thread import delete_thread

def threads_menu():
    print('Welcome to the Threads menu.')
    print('What would you like to do with the Threads menu?')

    print('1. List Threads\n')
    print('2. Create New Thread\n')
    print('3. Edit Thread\n')
    print('4. Delete Thread\n')

    user_input = user_input_int()

    if user_input == 1:
        list_thread_menu()
    elif user_input ==2:
        create_thread_menu()
    elif user_input_int ==3:
        edit_thread()
    else:
        delete_thread()