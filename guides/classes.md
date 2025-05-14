#### CS61A 
# `Classes` Review
#### Sean Villegas

- instance attributes refer to the specific attribute related to the instance 
- class attributes are globally accessible by all objects in the class 


### Making a new instance
```python
elisa = Staff('Elisa', 19) # dont include self when creating an instance because its implicitly passed 
```



### Modifying class attributes
- You can access class attributes from instances, but you cannot modify them from instances 

```python

# example 1
class Dog: 
    num_legs = 4
    def __init__(self, breed):
        self.bread = bread
    def drink_water(self):
        print('Woof!')

>>> Dog.num_legs
4

>>> Dog.num_legs = 8 
8 

>>> cat.num_legs
4


# example 2 

>>> def speak(a, b):
    print(b)

>>> Dog.growl = speak 
>>> my_dog = Dog("cat")
>>> my_dog.growl("roar")
roar! 


```




### You can assign functions to classes and things will behave as you think. Don’t assign functions to instances.



### You inherit when you want all the attributes and instances from the class, but want to modify it a bit



### `Repr` and `Str`

Takeaway: both return strings 
- repr returns the types value, repr always returns a string
- str identifies what the classes actual str is 
- calling the object will implicitly return the str or repr method of the class
    - without the repr and str it would give the memory address
- repr is python readable but it has a string repr 
- str is human readable 
- 




### Pointers
- is asks if the pointers are pointing to the same thing in memory 


### Translate the description into code 

