from menus.utilities import user_input_int
from menus.threads.list_thread_menu import list_thread_menu
from menus.threads.create_thread import create_thread_menu
from menus.threads.edit_thread import edit_thread
from menus.threads.delete_thread import delete_thread

def manage_threads_menu():
    print('Welcome to the Threads menu.')
    print('What would you like to do with the Threads menu?')

    print('1. List Threads')
    print('2. Create New Thread')
    print('3. Edit Thread')
    print('4. Delete Thread')

    user_input = user_input_int(4)

    if user_input == 1:
        list_thread_menu()
    elif user_input ==2:
        create_thread_menu()
    elif user_input ==3:
        edit_thread()
    else:
        delete_thread()