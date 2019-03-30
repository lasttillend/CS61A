# Final Review

# 2 Recursion
# 2.1 merge
def merge(s1, s2):
    """Merge two sorted lists.

    >>> merge([1, 3], [2, 4])
    [1, 2, 3, 4]
    >>> merge([1, 2], [])
    [1, 2]
    """
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    else:
        return [s2[0]] + merge(s1, s2[1:])

# 2.2 subset
def subset_sum(seq, k):
    """Returns whether there is a subset of the list that adds up to k.

    >>> subset_sum([2, 4, 7, 3], 5) # 2 + 3 = 5
    True
    >>> subset_sum([1, 9, 5, 7, 3], 2)
    False
    >>> subset_sum([1, 1, 5, -1], 3)
    False
    """
    if len(seq) == 0:
        return False
    elif seq[0] == k:
        return True
    else:
        return subset_sum(seq[1:], k - seq[0]) or subset_sum(seq[1:], k)

# 3 Trees
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

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

# 3.1 average
def average(t):
    """Returns the average value of all the nodes in t.

    >>> t0 = Tree(0, [Tree(1), Tree(2, [Tree(3)])])
    >>> average(t0)
    1.5
    >>> t1 = Tree(8, [t0, Tree(4)])
    >>> average(t1)
    3.0
    """
    def sum_helper(t):
        total, count = t.label, 1
        for b in t.branches:
            b_total, b_count = sum_helper(b)
            total += b_total
            count += b_count
        return total, count

    total, count = sum_helper(t)
    return total / count

# 6 Generators
# 6.1 accumulate
from operator import add, mul

def accumulate(iterable, f):
    """
    >>> list(accumulate([1, 2, 3, 4, 5], add))
    [1, 3, 6, 10, 15]
    >>> list(accumulate([1, 2, 3, 4, 5], mul))
    [1, 2, 6, 24, 120]
    """
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for el in it:
        total = f(total, el)
        yield total

# 6.2 repeated
def repeated(f):
    """Returns a generator that yields functions that are repeated applications of a one-argument function f.

    >>> double = lambda x: 2 * x
    >>> funcs = repeated(double)
    >>> identity = next(funcs)
    >>> double = next(funcs)
    >>> quad = next(funcs)
    >>> oct = next(funcs)
    >>> quad(1)
    4
    >>> oct(1)
    8
    >>> [g(1) for _, g in zip(range(5), repeated(lambda x: 2 * x))]
    [1, 2, 4, 8, 16]
    """
    # Wrong version
    # g = lambda x: x
    # while True:
    #     yield g
    #     g = lambda x: f(g(x))  # g changes, it does not point to the identity function when you try to call f on g(x)

    g = lambda x: x
    while True:
        yield g
        g = (lambda g: lambda x: f(g(x)))(g)  # using higher order function to store the old g
