class Item:
    def __init__(self, name, quantity, category):
        self.name = name
        self.quantity = quantity
        self.category = category

    def __repr__(self):
        return f"Item('{self.name}', {self.quantity}, '{self.category}')"
    
class GroceryList:
    def __init__(self, store_name):
        self.store_name = store_name 
        self.items = []

    def add_new_item(self, name, quantity, category):
        """Creates new Item with provided name, quantity, category. 
        Adds new item to lists items and returns it. If item with that name 
        exists, it returns None"""

                            # access item name for _ in the instance attribute of self.items
        existing_item_names = [item.name for item in self.items]
            # if the _ not in our variable list 
        if name not in existing_item_names:
                        # you call the Item class with parameters from add_new_item
            new_item = Item(name, quantity, category)
                    # append to self.items with our new_item variable 
            self.items.append(new_item) 
            return new_item # return the new item 
        
    def all_for_category(self, category): 
        """Returns list of all items for given category"""
        # return [for self.items if self.category == category]
        return [item for item in self.items if item.category == category]
    

"""
***ADD TO NOTES***

[<expression> for <variable> in <iterable>]

in list comprehension you can make the variable for looping anything, and to access its item.<instance attribute> 
you must adhere to previously defined dummy variable <item> expression
"""