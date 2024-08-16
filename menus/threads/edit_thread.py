from embroidery_thread import emb_thread
from menus.utilities import user_input_int

def edit_thread():
    print('What Thread Brand would you like to edit?')
# Listing the BRANDS.
    for x in range(0, len(emb_thread['brands'])):
        print(x+1,'.', emb_thread['brands'][x]['name'])
    user_input = user_input_int(len(emb_thread['brands']))

# Empty list to append(push) filtered threads 
    empty_thread_list = []

# Filtering through threads by BRAND.
    for thread in emb_thread['threads']:
        if thread['brand'] == user_input:
                empty_thread_list.append(thread)
    # For debugging purposes, can be deleted after 
    # print("empty_thread_list --> Printed from edit_thread File:", empty_thread_list)
    
# Selecting which thread to edit.
    print('Choose the Thread you would like to edit?')

    for x in range(0, len(empty_thread_list)):
        print(x+1,'.', empty_thread_list[x]['name'])

    user_input = user_input_int(len(empty_thread_list))

    print('What aspect of this Thread would you like to edit?')
# Keys that are not editable by user.
    block_list = ['alternatives']

# Prints keys for selected thread.
    thread_keys = list(empty_thread_list[user_input - 1].keys())
    for [index, key] in enumerate(thread_keys):
         if key in block_list:
              continue
         print(index + 1, '.', key.title())
    
    user_input = user_input_int(len(empty_thread_list[user_input-1]))
    selected_thread_key = thread_keys[user_input - 1]
    print(selected_thread_key, "Line 40")

    print("You are editing the Thread color: ", empty_thread_list[user_input-1])
    edited_thread = (input("Please enter the new thread color.")).title()

    if edited_thread.strip() == "":
        print('No edits were made.')
        ###### Needs to back to the brand menu at the beginning
    you_sure = input("Are you satisfied with the edits?")
        
    if you_sure.upper() == 'Y' or you_sure.upper() =='YES':
        empty_thread_list[user_input-1] = edited_thread
        print('You successfully changed the thread to: ', edited_thread)
    elif you_sure.upper() == 'N' or you_sure.upper() == 'NO':
        ###### Need to go back to edited_thread, line 28
        print('Start over, edit the thread name:')

    # For debugging purposes, can be deleted after 
    print('Printing from EDIT Thread', empty_thread_list)


# EDIT
# if number or symbols ONLY --> do not save

# NEED TO ADD:
# will need to go back to the beginning, the brand/thread list
# will need to go back to the edited_thread to edit again
# need to be able to exit the edit menu and go back at any time
# will need to edit thread by : name, length, etc.