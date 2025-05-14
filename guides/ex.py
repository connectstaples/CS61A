def paste(n):
    yield n
    for x in paste(n+1):
        yield 2 * x
    yield n

def copy(t, k):
    return [next(t) for x in range(k)]

copy(paste(0), 3)



s = [2, [5, 8], 11]
t = [1, 3, 5, 7, 9]

def add_t(x):
    if isinstance(x, list):
        return [add_t(y) for y in x]
    else: 
        return x + t.pop()

m = map(add_t, s) 


def f(this):
    that = this[1]
    def g(copy):
        that[0] = 4
        copy[0] = 5
        copy[1].append(6)
        print(copy)
    g(list(this))
    this.append(that)
    that.append(7)

t = [1, [2], 3]
f(t)
print(t) 


def nest(n):
    """Create a nested list.
    >>> nest(3)
    [[[[], []], [], [[], []]], [[[], []], [[], []]]]
    """

    s = []
    first = s
    for x in range(n):
        next_s = []
        s.append(next_s)
        s.append(next_s)
        s = next_s
    return first


""" Create a mega list that will create a pointer to the original team1
and team2 lists

recall: append mutates list and returns None


choices to choose from:

 [team1, team2]
 [team1] + [team2]
 [team1[0:], team2[0:]]
 [team1 + team2]
 [list(team1 + team2)]
 team1, team2
 [list(team1), list(team2)]
 team1 + team2
 team1 - team2
 team1 + team2[:]
 team1[:] + team2
 team1[:] + team2[:]
 team1 += team2

** Create a ultra list that points to its own individual list of the elements from
team1 & team2 **

choices to choose from:

 team1 + team2
 team1[:] + team2[:]
 team1 + team2[:]
 team1[:] + team2
 [team1, team2]
 [team1[0:], team2[0:]]
 [team1 + team2]
 [list(team1 + team2)]
 team1, team2
 [list(team1), list(team2)]
 team1 - team2
 [team1] + [team2]
 team1 += team2


team1 + team2
team1[:] + team2[:]
team1 + team2[:]
team1[:] + team2

[team1 + team2] # the outerbrackets create a sublist
[list(team1 + team2)] # the outerbrackets create a sublist


** Create a alpha list that is a pointer of the elements in team1 and team2,
but do not modify the original lists **

choices to choose from:

 [list(team1), list(team2)]
 [team1[0:], team2[0:]]
 [team1, team2]
 [team1 + team2]
 [list(team1 + team2)]
 team1, team2
 team1 + team2
 team1 - team2
 [team1] + [team2]
 team1 + team2[:]
 team1[:] + team2
 team1[:] + team2[:]
 team1 += team2

[list(team1), list(team2)]
[team1[0:], team2[0:]]


"""

team1 = [13, 15]
team2 = [18, 20]
mega = 2 

ultra = 2

alpha = 2




original_list = [1, [2, 3], 4]
shallow_copied_list = original_list[:]  # Creating a shallow copy using slicing

shallow_copied_list[0] = 10  # Modifying an element in the shallow copy
print(f"Original list: {original_list}")  # Output: Original list: [1, [2, 3], 4]
print(f"Shallow copied list: {shallow_copied_list}")  # Output: Shallow copied list: [10, [2, 3], 4]

shallow_copied_list[1][0] = 20  # Modifying a mutable element (inner list)
print(f"Original list: {original_list}")  # Output: Original list: [1, [2, 20], 4]
print(f"Shallow copied list: {shallow_copied_list}")  # Output: Shallow copied list: [10, [2, 20], 4]



"""
Depth of trees based on copy 
"""

def paste(n, depth=2):
    if depth == 0:
        return  # Base case: stop recursion at depth 0
    yield n
    for x in paste(n + 1, depth - 1):
        yield 2 * x
    yield n

def copy(t, k):
    return [next(t) for x in range(k)]


from datascience import Table

# Create a sample table
tbl = Table().with_columns(
    "Name", ["Alice", "Bob", "Charlie"],
    "Age", [24, 19, 22],
    "Major", ["CS", "Math", "Physics"]
)

tbl.show()

row = tbl.row(1)  # Get the second row (index starts at 0)
age_of_bob = row.item("Age")
print(age_of_bob) # _______