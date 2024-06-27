from embroidery_thread import emb_thread
from menus.brands.create_brand import create_brand_menu
from menus.utilities import user_input_int

def select_thread():
    print('Select Thread Brand')

    if len(emb_thread['brands']) == 0:
        print('Oops! There are no thread brands available, create one now!')
        create_brand_menu()

    for x in range(0, len(emb_thread['brands'])):
        print(x+1,'.', emb_thread['brands'][x])

    user_input = user_input_int(len(emb_thread['brands']))
    # For debugging purposes, can delete when done
    print(str(emb_thread['brands'][user_input-1]) + 'select_thread()')
    return emb_thread['brands'][user_input-1]