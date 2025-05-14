class Transaction:
    def __init__(self, id, before, after):
        self.id = id
        self.before = before
        self.after = after

    def changed(self):
        """Return whether the transaction resulted in a changed balance."""
        "*** YOUR CODE HERE ***"
        return self.before != self.after 

    def report(self):
        """Return a string describing the transaction.

        >>> Transaction(3, 20, 10).report()
        '3: decreased 20->10'
        >>> Transaction(4, 20, 50).report()
        '4: increased 20->50'
        >>> Transaction(5, 50, 50).report()
        '5: no change'
        """
        msg = 'no change'
        if self.changed():
            if self.before < self.after:
                msg = 'increased ' + str(self.before) + '->' + str(self.after)
            else:
                msg = 'decreased ' + str(self.before) + '->' + str(self.after)
        return str(self.id) + ': ' + msg



class BankAccount:
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = [] # empty list created

    def deposit(self, amount):
        before = self.balance # assignment of before to instance attribute of balance
        self.balance = self.balance + amount # computation for balance
        self.transactions.append(Transaction(len(self.transactions), before, self.balance)) # adding the length of the transaction, int, and int to the list for each unique instance
        return self.balance

    def withdraw(self, amount):
        before = self.balance  # assignment of before to instance attribute of balance within this frame 
        if amount > self.balance:
            # Record the failed transaction before returning
            self.transactions.append(Transaction(len(self.transactions), before, before))
            return 'Insufficient funds'
        self.balance = self.balance - amount
        self.transactions.append(Transaction(len(self.transactions), before, self.balance))
        return self.balance


class Email:
    """An email has the following instance attributes:

        msg (str): the contents of the message
        sender (Client): the client that sent the email
        recipient_name (str): the name of the recipient (another client)
    """
    def __init__(self, msg, sender, recipient_name):
        self.msg = msg
        self.sender = sender
        self.recipient_name = recipient_name

class Server:
    """Each Server has one instance attribute called clients that is a
    dictionary from client names to client objects.

    >>> s = Server()
    >>> # Dummy client class implementation for testing only
    >>> class Client:
    ...     def __init__(self, server, name):
    ...         self.inbox = []
    ...         self.server = server
    ...         self.name = name
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> s.register_client(a) 
    >>> s.register_client(b)
    >>> len(s.clients)  # we have registered 2 clients
    2
    >>> all([type(c) == str for c in s.clients.keys()])  # The keys in self.clients should be strings
    True
    >>> all([type(c) == Client for c in s.clients.values()])  # The values in self.clients should be Client instances
    True
    >>> new_a = Client(s, 'Alice')  # a new client with the same name as an existing client
    >>> s.register_client(new_a)
    >>> len(s.clients)  # the key of a dictionary must be unique
    2
    >>> s.clients['Alice'] is new_a  # the value for key 'Alice' should now be updated to the new client new_a
    True
    >>> e = Email("I love 61A", b, 'Alice')
    >>> s.send(e)
    >>> len(new_a.inbox)  # one email has been sent to new Alice
    1
    >>> type(new_a.inbox[0]) == Email  # a Client's inbox is a list of Email instances at index 0
    True
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Append the email to the inbox of the client it is addressed to.
            email is an instance of the Email class.
        """
        self.clients[email.recipient_name].inbox.append(email)
    #   instance.clients[list]

    def register_client(self, client):
        """Add a client to the clients mapping (which is a 
        dictionary from client names to client instances).
            client is an instance of the Client class.
        """
        self.clients[client.name] = client # update

class Client:
    """A client has a server, a name (str), and an inbox (list).

    >>> s = Server() # object instance 
    >>> a = Client(s, 'Alice') # instance attribute of Alice
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob') 
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox) # in a shared list with a pointer 
    2
    >>> b.inbox[1].msg 
    'CS 61A Rocks!'
    >>> b.inbox[1].sender.name # accessing special instance self name
    'Alice'
    """
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name
        server.register_client(self)

    def compose(self, message, recipient_name):
        """Send an email with the given message to the recipient.
        
        class Email:
            An email has the following instance attributes:

                msg (str): the contents of the message
                sender (Client): the client that sent the email
                recipient_name (str): the name of the recipient (another client)

            def __init__(self, msg, sender, recipient_name):
                self.msg = msg
                self.sender = sender
                self.recipient_name = recipient_name
        """

        email = Email(message, self, recipient_name)
        self.server.send(email)


class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint() # instance attribute 
    >>> mint.year # mints class global variable 
    2025
    >>> dime = mint.create(Dime) # inheritance 
    >>> dime.year
    2025
    >>> Mint.present_year = 2105  # Time passes
    >>> nickel = mint.create(Nickel) # inheritance 
    >>> nickel.year     # The mint has not updated its stamp yet
    2025
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2105
    >>> Mint.present_year = 2180     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2025 # class attribute 

    def __init__(self):
        self.update()

    def create(self, coin):
        "*** YOUR CODE HERE ***"
        """Creates and returns an instance of the coin subclass stamped with the mint's year."""
        return coin(self.year)
        

    def update(self):
        "*** YOUR CODE HERE ***"
        """Sets the mint's year stamp to the current Mint.present_year."""
        self.year = Mint.present_year

# Inheritance example

"""
>>> c = Nickel(1990)
>>> c.year
1990
>>> c.cents
5
"""
class Coin:
    cents = None # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        """Returns cents plus one extra cent for each year beyond 50."""
        age = Mint.present_year - self.year
        if age > 50:
            return self.cents + (age - 50)
        return self.cents

class Nickel(Coin): # each class cent based on Name, Inheritance 
    cents = 5

class Dime(Coin): # each class cent based on Name, Inheritance 
    cents = 10

