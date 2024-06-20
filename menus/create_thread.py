from embroidery_thread import emb_thread
# CREATE THREAD
## If you select OPTION 2

def create_thread_menu():
    print('Add a New Thread to Inventory')
    # create thread from emb_Thread and then add to the list
    # creating a new dictionary --> new object
    # at the end then you would append to emb_thread

    new_thread = {}

    sku = input('SKU: ')
    new_thread['sku'] = sku

    item = input('Item #: ')
    new_thread['item'] = item

    name = input('Name: ')
    new_thread['name'] = name.title()

    type= input('Thread Type: ')
    new_thread['type'] = type.title()

    ## Select M/YDS --> Offer that as an option
    length = input('Length: ')
    new_thread['length'] = length

    ##Does this need to be its own function?
    print('Select Thread Brand')
    for x in range(0, len(emb_thread['brands'])):
        print(x+1,'.', emb_thread['brands'][x])
    brand_choice_input = input('Select a brand number.')
    
    try:
        brand_choice_input = int(brand_choice_input)
        print('Hooray - Brand Choice Selected')
    except ValueError:
        ## How do I get to the selection again without triggering the thread menu()
        ## Can I just put {brand_choice_input} in a fstring?
        print(f"Please select a number.")
    
    new_thread['brand'] = emb_thread['brands'][brand_choice_input-1]

    print(emb_thread)

    emb_thread['threads'].append(new_thread)

    print('THREAD menu')