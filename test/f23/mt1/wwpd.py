"""
>>> dog(cat)
Error
>>> dog()
5 # is redefined at the end. Notice how 3 is defined before the call to the function 
>>> print((lambda dog: print(dog()))(lambda: 6))
6 ## remember not to print function for lambda's value. Why isn't 5 printed for dog()? Because the lambda: 6 is passed through dog(), thus printing 6
None
>>> hog()
4, 5
"""


cat = 3 
def dog():
    return cat
def hog():
    cat = 4
    print(cat, dog()) 
cat = 5 

# print((lambda dog: print(dog))(lambda: 6)) # notice difference here 
# print((lambda dog: print(dog()))(lambda: 6)) # because there is a dog() call, this means it evaluates as a call expression