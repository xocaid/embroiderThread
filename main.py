from menus.create_brand import create_brand_menu
from menus.create_thread import create_thread_menu
from embroidery_thread import emb_thread

def main():
    print('What action do you want to perform?\n')
    print('1. Create thread brand\n')
    print('2. Add thread to inventory\n')
    print('3. List inventory\n')
    user_input = input('Enter a number.')

    ## Can delete once done - only for debugging purposes
    print(user_input)

    try:
        user_input = int(user_input)
    except ValueError:
        print(f"See you next time.{user_input}")
        return

    if user_input == 1:
        create_brand_menu()
    elif user_input == 2:
        create_thread_menu()
    elif user_input == 3:
         print(emb_thread)
    else:
        print('See you next time.')

main()
