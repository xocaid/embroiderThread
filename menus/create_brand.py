from embroidery_thread import emb_thread

## If you select OPTION 1
# Create Brand
def create_brand_menu():
    print('Create a Thread Brand')
    name = input('Name: ')
    emb_thread['brands'][0]['name'] = name.title()

## Can delete once done - only for debugging purposes
    print(emb_thread)