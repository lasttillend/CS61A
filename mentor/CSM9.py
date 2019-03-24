# Generators and Streams

# 1 Iterators and Generators
# 1.
def foo():
    a = 0
    if a < 10:
        print("Hello")
        yield a
        print("World")

for i in foo():
    print(i)

# 2.
def foo():
    a = 0
    while a < 10:
        print("Hello")
        yield a
        print("World")
        a += 1

# 3.
def hailstone_sequence(n):
    """
    >>> hs_gen = hailstone_sequence(10)
    >>> next(hs_gen)
    10
    >>> next(hs_gen)
    5
    >>> for i in hs_gen:
            print(i)
    16
    8
    4
    2
    1
    """
    yield n
    if n == 1:
        return
    elif n % 2 == 0:
        yield from hailstone_sequence(n // 2)
    else:
        yield from hailstone_sequence(3 * n + 1)

# 4.
class Tree:
    def __init__(self, label, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.label = label
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)

    def is_leaf(self):
        return not self.branches

def tree_sequence(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(5)]), Tree(3, [Tree(4)])])
    >>> print(list(tree_sequence(t)))
    [1, 2, 5, 3, 4]
    """
    yield t.label
    if t.is_leaf():
        return
    for b in t.branches:
        yield from tree_sequence(b)

# 4 Challenge Question
# 1. Write a generator that takes in a tree and yields each possible path from root to leaf, represented as a list of that path. Use the objected-oriented representation of treees in your solution.
def all_paths(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(5)]), Tree(3, [Tree(4)])])
    >>> print(list(all_paths(t)))
    [[1, 2, 5], [1, 3, 4]]
    """
    if t.is_leaf():
        yield [t.label]
    for b in t.branches:
        for path in all_paths(b):
            yield [t.label] + path

