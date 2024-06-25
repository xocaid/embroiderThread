from embroidery_thread import emb_thread

# Create Brand
def create_brand_menu():
    print('Create a Thread Brand')

    new_brand = {}

    name = input('Name: ')
    new_brand['name'] = name.title()
    new_brand['id'] = generate_brand_id()
    emb_thread['brands'].append(new_brand)

def generate_brand_id():
    if len(emb_thread['brands']) == 0:
        return 1
    
    return emb_thread['brands'][-1]['id']+1
