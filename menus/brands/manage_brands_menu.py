from menus.utilities import user_input_int
from menus.brands.list_brand_menu import list_brand_menu
from menus.brands.create_brand import create_brand_menu
from menus.brands.edit_brand import edit_brand
from menus.brands.delete_brand import delete_brand_menu

def manage_brands_menu():
    print('Welcome to the Brands menu.')
    print('What would you like to do with the Brands menu?')

    print('1. List Brands')
    print('2. Create New Brand')
    print('3. Edit Brand')
    print('4. Delete Brand')

    user_input = user_input_int()

    if user_input == 1:
        list_brand_menu()
    elif user_input ==2:
        create_brand_menu()
    elif user_input ==3:
        edit_brand()
    else:
        delete_brand_menu()
