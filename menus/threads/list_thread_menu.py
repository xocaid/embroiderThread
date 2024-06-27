from embroidery_thread import emb_thread
from menus.utilities import user_input_option

def list_thread_menu():
    print('What Thread list would you like to see?')

    for x in range(0, len(emb_thread['brands'])):
        print(x+1,'.', emb_thread['brands'][x]['name'])

    print('A. Show all')
    user_input = user_input_option(['A'],len(emb_thread['brands']) )


    show_all = user_input == 'A'    
    if show_all:
        brand_listed = None
    else:
        brand_listed = emb_thread['brands'][user_input-1]

    for thread in emb_thread['threads']:
        if show_all or thread['brand'] == brand_listed['id']:
            print(thread['name'])
    

    ##Longer version of above code
    # for i in range(0, len(emb_thread['threads'])):
    #     threads_array = emb_thread['threads']
    #     thread = threads_array[i]

    #     # current thread == selected brand
    #     if thread['brand'] == brand_listed['id']:
    #         print(thread['name'])

    # create a new function alongside user_input_int() 
    # same logic in the user_input_int()
