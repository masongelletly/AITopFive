
# For simplicity, we'll use a dictionary to store data in memory
# In a real application, this might be a database or a file

data = {
    'categories': {},  # Stores categories and their top 5 lists
}

def add_category(category_name):
    '''Adds a new category.'''
    if category_name in data['categories']:
        return False
    data['categories'][category_name] = []
    return True

def get_categories():
    '''Returns a list of all categories.'''
    return list(data['categories'].keys())

def add_to_list(category_name, item):
    '''Adds an item to the top 5 list of a category.'''
    if category_name not in data['categories']:
        return False
    if len(data['categories'][category_name]) >= 5:
        return False
    data['categories'][category_name].append(item)
    return True

def get_top_five(category_name):
    '''Returns the top 5 list for a category.'''
    return data['categories'].get(category_name, [])
