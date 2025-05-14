class Item:
    """
    >>> broccoli = Item("broccoli", 1, "veggies")
    >>> broccoli.name
    'broccoli'
    >>> broccoli.quantity
    1
    >>> broccoli.category
    'veggies'
    >>> broccoli
    Item("broccoli", 1, "veggies")
    """

    def __init__(self, name, quantity, category):
        self.name = name
        self.quantity = quantity
        self.category = category

    def __repr__(self):
        return f"Item('{self.name}', {self.quantity}, '{self.category}')"
    
class GroceryList:
    """
    >>> tjlist = GroceryList('Trader Joes')
    >>> tjlist.store_name
    'Trader Joes'
    >>> tjlist.items
    []
    >>> tjlist.add_new_item('Truffle Chips', 2, 'snacks')
    Item('Truffle Chips', 2, 'snacks')
    >>> tjlist.items
    [Item('Truffle Chips', 2, 'snacks')]
    >>> tjlist.add_new_item('Zesty Popcorn', 1, 'snacks')
    Item('Zesty Popcorn', 1, 'snacks')
    >>> tjlist.items
    [Item('Truffle Chips', 2, 'snacks'), Item('Zesty Popcorn', 1, 'snacks')]
    >>> tjlist.add_new_item('Truffle Chips', 3, 'snacks')
    >>> tjlist.add_new_item('Apple', 5, 'fruits')
    Item('Apple', 5, 'fruits')
    >>> tjlist.all_for_category('snacks')
    [Item('Truffle Chips', 2, 'snacks'), Item('Zesty Popcorn', 1, 'snacks')]
    >>> tjlist.all_for_category('fruits')
    [Item('Apple', 5, 'fruits')]
    """

    def __init__(self, store_name):
        self.store_name = store_name 
        self.items = []

    def add_new_item(self, name, quantity, category):
        """Creates new Item with provided name, quantity, category. 
        Adds new item to lists items and returns it. If item with that name 
        exists, it returns None"""
        existing_item_names = [item.name for item in self.items]

        if name not in existing_item_names:
            new_item = existing_item_names(self.items)
            existing_item_names.append.Item(new_item)
            return new_item  

    def all_for_category(self, category): 

        """Returns list of all items for given category"""
        # return [for self.items if self.category == category]
        return [item for item in self.items if item.category == category]
    
class ShareableList(GroceryList):
    """Inherit from GroceryList. This class allows you to have a shopping list shared by multiple users. Each instance of
    ShareableList has same instance variables as GroceryList(store_name and items) but also has two additional instance variables
    
    - collaborators is a list of email addresses, specified when constructing the instance
    - items_by_adder is a dictionary tracking WHICH email addresses added which item. 
    Starts off aas a dictionary with a key for each email address mapped to it an empty list

    >>> roomie_list = ShareableList('Trader Joes', ['don@key.com', 'star@burns.com'])
    >>> roomie_list.store_name
    'Trader Joes'
    >>> roomie_list.items
    []
    >>> roomie_list.collaborators
    ['don@key.com', 'star@burns.com']
    >>> roomie_list.items_by_adder
    {'don@key.com': [], 'star@burns.com': []}
    >>> roomie_list.add_new_items('Wasabi Peas', 100, 'snacks', 'don@key.com')
    Item('Wasabi Peas', 100, 'snacks')
    >>> roomie_list.items_by_adder
    {'don@key.com': [Item('Wasabi Peas', 100, 'snacks')], 'star@burns.com': []}
    """
    
    def __init__(self, store_name, collaborators):
        super().__init__(store_name)
        self.collaborators = collaborators 
        self.items_by_adder = {collaborators: [] for collaborators in self.collaborators}

    def add_new_item(self, name, quantity, category, adder):
        
        new_item = super().add_new_item(name, quantity, category)
        if new_item: 
            self.items_by_adder[adder].append(new_item)
        return new_item 


