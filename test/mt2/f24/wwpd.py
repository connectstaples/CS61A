"""
wwpd?

>>> crow.branches[0].label # 9 
0 

"""

class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
            self.branches = list(branches)
    def is_leaf(self):
        return not self.branches


scare = Tree(0, [Tree(4), Tree(5, [Tree(10)]), Tree(2)])
crow = Tree(9, [scare, Tree(7, [Tree(6)])])

def climb(t, f):
    if t.is_leaf():
        return [t.label]
    return [t.label] + climb(max(t.branches, key=f), f)

def run(t):
    if t.is_leaf():
        return t.label
    else:
        return max(map(run, t.branches))
    
def hide(t):
    return t.label

jump = {(2 * x - 1): x for x in range(50)}


## other

t = Tree(3, [Tree(1, [Tree(4), Tree(1)]), Tree(5, [Tree(9)])])
