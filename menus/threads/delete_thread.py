from menus.utilities import user_input_int
from embroidery_thread import emb_thread

## Main function: To delete thread from the database
def delete_thread():
    print('Delete Thread from Inventory')
    print('What thread would you like to delete?')
    for x in range(0, len(emb_thread['threads'])):
        print(x+1,'.', emb_thread['threads'][x]['name'])

    user_input = user_input_int(len(emb_thread['threads'])) #5
    # call pop method & save to variable
    deleted_thread = emb_thread['threads'].pop(user_input-1)
    #print statement with pop value
    print(f'Successfully deleted the color: {deleted_thread['name']}')

## Delete another thread
def loop_delete_thread():
    while True:
        delete_thread()
        user_input =input("Would you like to delete another thread?")
        if user_input.lower() == "yes" or user_input.lower() == "y":
            continue
        else:
            break