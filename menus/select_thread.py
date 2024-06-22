from embroidery_thread import emb_thread

def select_thread():
    print('Select Thread Brand')
    for x in range(0, len(emb_thread['brands'])):
        print(x+1,'.', emb_thread['brands'][x])
    
    brand_choice_input = input('Select a brand number.')
    
    try:
        brand_choice_input = int(brand_choice_input)
        print('Hooray - Brand Choice Selected')
    except ValueError:
        ## How do I get to the selection again without triggering the thread menu()
        print("Please select a number.")

        # while loop, the action that you want to repeat until you get what you want
        # what action do you want to repeat?
        # wrap line 7-15
        # While TRUE --> run until you get an integer
        # Break out of while loop --> 'break' OR 'return' from inside of while loop
            # You will break out once the integer is entered

    
    return emb_thread['brands'][brand_choice_input-1]
