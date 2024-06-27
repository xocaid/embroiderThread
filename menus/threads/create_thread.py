# CREATE THREAD
from embroidery_thread import emb_thread
from menus.threads.select_thread import select_thread

def create_thread_menu():
    print('Add a New Thread to Inventory')

    new_thread = {}

    sku = input('SKU: ')
    new_thread['sku'] = sku

    item = input('Item #: ')
    new_thread['item'] = item

    name = input('Name: ')
    new_thread['name'] = name.title()

    type= input('Thread Type: ')
    new_thread['type'] = type.title()

    length = input('Length: ')
    length_unit = input('m or yd?')
    if length_unit.upper() == 'M':
        new_thread['length'] = length + 'M'
    else:
        new_thread['length'] = length + 'Yds'
    
    new_thread['brand'] = select_thread()
    emb_thread['threads'].append(new_thread)

    print('New Thread Created: ' + str(emb_thread['threads'][-1]))