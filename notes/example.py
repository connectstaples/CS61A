class Chef:
   """A chef earns tips when they cook a dish or when a dish they prepped is cooked by
   another chef.

    >>> alice = Chef()
    >>> bob = Chef()
    >>> k = Kitchen([alice, bob])
    >>> alice.prep('Soup')
    >>> bob.prep('Soup')
    >>> alice.cook('Soup', 4)  # 2 dollars to alice & 2 to bob
    >>> bob.cook('Soup', 6)    # 3 dollars to bob & 3 to alice

    >>> alice.prep('Salad')
    >>> bob.prep('Salad')
    >>> bob.cook('Pasta', 2)   # 2 to bob (no one prepped Pasta, so full tip to cooker)
    >>> alice.cook('Salad', 8) # 4 to alice & 4 to bob
    >>> [alice.tips, bob.tips]
    [9.0, 9.0]
    """
    def __init__(self):
        self.tips = 0  
        self.kitchen = None

    def prep(self, dish):
        """prep method takes a string `dish` and registers it in the `Kitchen` class where          they work
        """
        self.kitchen.dishes[dish] = self 

    def cook(self, dish, tip):
        """
        cook method takes a string `dish` that has been prepped in their kitchen, and
        number `tip`. The chef who cooked the dish and the Chef who most recently prepped
        the dish split the tip. If no chef prepped dish, cooking chef recives full tip
        """
        self.tips += tip / 2
        self.kitchen.dishes[dish].tips += tip / 2

class Kitchen:
    """A kitchen tracks dishes prepped by chefs who work there."""
    def __init__(self, chefs):
        self.dishes = {}
        for chef in chefs:
            chef.kitchen = self
