from .delete_brand import delete_brand_menu

def manage_brands_menu():
    print('What would you like to do with brands?')
    print('')
    print('1. List brands')
    print('2. Create new brand')
    print('3. Edit brand')
    print('4. Delete brand')
    print('')

    user_choice = input('Action: ')

    if user_choice == "4":
        delete_brand_menu()
