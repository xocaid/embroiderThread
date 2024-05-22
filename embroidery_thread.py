## If you select OPTION 3
emb_thread={'brands': [{
    'id': None, 
    'name':None}],
            'threads': [{
                'sku':None,
                'item':None,
                'name':None,
                'type':None,
                'length':None,
                'brand':None,
                'alternatives':[{
                    'brand':None,
                    'item':None
                }]
            }]
}

## If you select OPTION 1
def brand_menu():
    print('Create a Thread Brand')
    name = input('Name: ')
    emb_thread['brands'][0]['name'] = name.title()

## Can delete once done - only for debugging purposes
    print(emb_thread)

## If you select OPTION 2
def thread_menu():
    print('Add a New Thread to Inventory')

    sku = input('SKU: ')
    emb_thread['threads'][0]['sku'] = sku

    item = input('Item #: ')
    emb_thread['threads'][0]['item'] = item

    name = input('Name: ')
    emb_thread['threads'][0]['name'] = name.title()

    type= input('Thread Type: ')
    emb_thread['threads'][0]['type'] = type.title()

## Select M/YDS --> Offer that as an option
    length = input('Length: ')
    emb_thread['threads'][0]['length'] = length

    ##Does this need to be its own function?
    print('Select Thread Brand')
    brands = ['New Brothread', 'ThreadArt','Madeira']
    for x in range(0, len(brands)):
        print(x+1,'.', brands[x])
    brand_choice_input = input('Select a brand number.')
    
    try:
        brand_choice_input = int(brand_choice_input)
        print('Hooray - Brand Choice Selected')
    except ValueError:
        ## How do I get to the selection again without triggering the thread menu()
        ## Can I just put {brand_choice_input} in a fstring?
        print(f"Please select a number.")
    
    if brand_choice_input == 1:
        emb_thread['threads'][0]['brand'] = brand_choice_input
    if brand_choice_input ==2 : 
        emb_thread['threads'][0]['brand'] = brand_choice_input 
    if brand_choice_input == 3:
        emb_thread['threads'][0]['brand'] = brand_choice_input



    print(emb_thread)

    print('THREAD menu')


2


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
        brand_menu()
    elif user_input == 2:
        thread_menu()
    elif user_input == 3:
         print(emb_thread)
    else:
        print('See you next time.')

main()



