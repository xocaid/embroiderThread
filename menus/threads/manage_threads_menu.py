from menus.utilities import user_input_int
from menus.threads.list_thread_menu import list_thread_menu
from menus.threads.create_thread import create_thread_menu
from menus.threads.edit_thread import edit_thread
from menus.threads.delete_thread import loop_delete_thread
from menus.utilities import which_menu
from menus.utilities import crud_ops
from menus.utilities import loop_crud_ops

def manage_threads_menu():
    print('Welcome to the Threads menu.')
    print('What would you like to do with the Threads menu?')

# Store the array to reuse list items for which_menu()
    menu_options = crud_ops('Threads')
    loop_crud_ops(menu_options)

    user_input = user_input_int(4)
    if user_input == 1:
        menu_fxn_to_call = list_thread_menu
    elif user_input ==2:
        menu_fxn_to_call =create_thread_menu
    elif user_input ==3:
        menu_fxn_to_call =edit_thread
    elif user_input ==4:
        menu_fxn_to_call =loop_delete_thread
        print('From: Manage_Threads_Menu: Loop delete thread')
        
    menu_fxn_to_call()

    which_menu(menu_fxn_to_call,manage_threads_menu, menu_options[user_input - 1], 'Threads')