"""" WWPD exercise. 
>>> choose(one + one)
A
B
E

>>> which()()
3 

"""

one = 1

def choose(one):
    if big(one):
        print('A')
        if huge(one):
            print('B')
        elif big(one) or huge(one): # skip this when calling choose(one + one) because truthy value is already satisfied  
            print('C')
        if big(one) or print('D'):  # evaluate if statement again
            print('E')
        else: 
            print('F') # skip else statement 

big = lambda x: x >= one
huge = lambda x: x > one

def which():
    one = 3
    def this():
        return one
        return one + 1 # unreachable, not used
    return this
    one = 4  # redundant re-assignment # ones value stays 3 because this is not reachable 



def example():
    return 5
    print("This will never run")  # Unreachable code