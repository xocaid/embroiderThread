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
# print(emb_thread)

def main():
    print('What action do you want to perform?\n Press any key to exit.\n')
    print('1. Create thread brand\n')
    print('2. Add thread to inventory\n')
    print('3. List inventory\n')
    user_input = input('Enter a number.')

    print(user_input)

    try:
        user_input = int(user_input)
    except ValueError:
        print('See you next time.')
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

## If you select OPTION 1
##Need to store the input
def brand_menu():
    print('Create a Thread Brand')
    name = input('Name: ')
    print(f"BRAND menu now has {name}")

## If you select OPTION 2
## Need to store the input
def thread_menu():
    print('Add a New Thread to Inventory')
    sku = input('SKU: ')
    item = input('Item #: ')
    name = input('Name: ')
    type= input('Type: ')
    length = input('Length: ')
    ##Does this need to be its own function?
    print('Brand')
    brand_choice = print('1. New Brothread')
    brand_choice = print('2. ThreadArt')
    brand_choice = print('3. Madeira')
    brand_choice_input = input('Select a brand number.')

## How do I exit here if I want to quit here OR GO BACK?
    try:
        brand_choice_input = int(brand_choice_input)
        ## Why is this line not printing?
        print('Hooray - Brand Choice Selected')
    except ValueError:
        ## How do I get to the selection again without triggering the thread menu()
        ## Can I just put {brand_choice_input} in a fstring?
        print(f"Please select a number.")

    print('THREAD menu')