class Cat: 
    """
    >>> c = Cat(3)
    >>> c
    <__main__.Cat object at 0x103086510>
    >>> c.legs
    3
    >>> c.legs = 8 
    >>> c.legs
    8 
    >>> c.species
    'feline'
    >>> c.species = 'gato'
    >>> c.species 
    'gato'
    >>> d = Cat(5)
    >>> d.species
    'feline'
    """
    species = 'feline' 

    def __init__(self, legs, display):
        self.legs = legs
        self.display = display
    def __repr__(self):
        """displays when you type the bound object variable"""
        return f'I am a {self.species} with {self.legs} legs'
    def __str__(self):
        return f'{self.display}, {self.display} \n ### You found out how str works! ###'
    

"""
>>> d = Cat(3, 'Test')
>>> d
I am a feline with 3 legs
>>> print(d)
Test, Test 
 ### You found out how str works! ###
>>> str(d)
'Test, Test \n ### You found out how str works! ###'
>>> 
"""

### unbound and bound calling of methods ###

class Dog:
    def woof(self):
        print("woof")

a = Dog() 
unbound = Dog.woof
# explictly pass in c as self
unbound(a)  # Dog.woof(c)

bound = a.woof
bound()  # automatically pass in self


class Cat:
    def meow(self):
        print("meow")

c = Cat() 
unbound = Cat.meow
# explictly pass in c as self
unbound(c)  # Cat.meow(c)

bound = c.meow
bound()  # automatically pass in self


### Dynamic Method Assignment ###
"""
When you assign a plain function to a class, and then call it on an instance, Python turns it into a bound method, automatically passing the instance (self) as the first argument.

So the function gets wrapped as if it were a method, even though you didn’t define it that way inside the class.

"""


class Robot:
  """
  >>> def talk(a, b):
    ...    print(b)
    >>> Robot.speak = talk
    >>> iam = Robot('binary')
    >>> iam.speak("I am Mr. Robot”)
    I am Mr. Robot
  """
  def __init__(self, ctf):
    self.ctf = ctf
  def hack(self):
    print("Live for this shit")


"""
>>> iam = Robot('binary')
>>> def huh(self, other):
        return f'{self.ctf} is {other}'
>>> iam.uhh = huh
>>> iam.uhh('god')
...
>>> Robot.uhh(iam, 'god')
...
"""

"""
>>> Object
>>> "yay"
'yay'
>>> Tree(1, [Tree(2)])
Tree(1, [Tree(2)])
"""


"""
>>> print(Object)
"""


class Dress: 
   """What color is the dress?
   """
   seen = 0 
   color = None
   def __init__(self, color):
      self.color = color 
      self.seen = 0 
    def look(self):
      ____________ = ____________
      ____________ = ____________
      if ____________: 
            ____________ = ____________
        return ____________
    else:
        ____________ = ____________
   