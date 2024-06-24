from embroidery_thread import emb_thread
from menus.create_brand import create_brand_menu

def select_thread():
    print('Select Thread Brand')

    if len(emb_thread['brands']) == 0:
        print('Oops! There are no thread brands available, create one now!')
        return create_brand_menu()

    for x in range(0, len(emb_thread['brands'])):
        print(x+1,'.', emb_thread['brands'][x])

    while True: 
        brand_choice_input = input('Select a brand number.')
    
        try:
            brand_choice_input = int(brand_choice_input)
            print('Hooray - Brand Choice Selected')
            return emb_thread['brands'][brand_choice_input-1]
        
        except ValueError:
            print("Please select a number.")