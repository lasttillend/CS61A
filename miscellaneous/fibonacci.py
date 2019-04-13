# Fibonacci iteratively
def fib_i(n):
    prev, curr = 0, 1
    i = 0
    while i < n:
        prev, curr = curr, prev + curr
        i += 1
    return prev

print("Fibonacci iteratively:")
for k in range(10):
    print(fib_i(k))

# Fibonacci recursively
def fib_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_r(n - 1) + fib_r(n - 2)

print("Fibonacci recursively:")
for k in range(10):
    print(fib_r(k))

# Fibonacci using memoization
def fib_memo(n):
    """
    Takes in a number, n, and computes the nth fibonacci
    number recursively. To save time, it will only compute
    each value once and store it in a dictionary. We will
    define fib_memo(0) = 0 and fib_memo(1) = 1.

    >>> fib_memo(3)
    2
    >>> fib_memo(100)
    354224848179261915075   # this should take less than a second
    """
    memo = {}
    def fib_helper(n):
        if n in memo:
            return memo[n]
        if n <= 1:
            memo[n] = n
            return n
        memo[n] = fib_helper(n - 1) + fib_helper(n - 2)
        return memo[n]
    return fib_helper(n)

# Fibonacci iterator
class Fibonacci_i:
    """
    >>> f = Fibonacci_i()
    >>> i = iter(f)
    >>> next(i)
    0
    >>> next(i)
    1
    >>> next(i)
    1
    >>> next(i)
    2
    """
    def __init__(self):
        self.prev, self.curr = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        tmp = self.prev
        self.prev, self.curr = self.curr, self.curr + self.prev
        return tmp

# Finonacci iterator using a generator function
class Fibonacci_g:
    """
    >>> f = Fibonacci_g()
    >>> i = iter(f)
    >>> next(i)
    0
    >>> next(i)
    1
    >>> next(i)
    1
    >>> next(i)
    2
    """
    def __iter__(self):
        prev, curr = 0, 1
        while True:
            yield prev
            prev, curr = curr, prev + curr

# Fibonacci tree
class Tree:
    """A tree with label as its label value."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def is_leaf(self):
        return not self.branches

def fib_tree1(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left, right = fib_tree1(n - 2), fib_tree1(n - 1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])

# Fibonacci binary tree
class BTree(Tree):
    """A tree with exactly two branches, which may be empty."""
    empty = Tree(None)

    def __init__(self, label, left=empty, right=empty):
        for b in (left, right):
            assert isinstance(b, BTree) or b is BTree.empty
        Tree.__init__(self, label, [left, right])

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return [self.left, self.right] == [BTree.empty] * 2

    def __repr__(self):
        if self.is_leaf():
            return 'BTree({0})'.format(self.label)
        elif self.right is BTree.empty:
            left = repr(self.left)
            return 'BTree({0}, {1})'.format(self.label, left)
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BTree.empty:
                left = 'BTree.empty'
            template = 'BTree({0}, {1}, {2})'
            return template.format(self.label, left, right)

def fib_tree2(n):
    """Fibonacci binary tree.

    >>> fib_tree(3)
    BTree(2, BTree(1), BTree(1, BTree(0), BTree(1)))
    """
    if n == 0 or n == 1:
        return BTree(n)
    else:
        left = fib_tree2(n - 2)
        right = fib_tree2(n - 1)
        fib_n = left.label + right.label
        return BTree(fib_n, left, right)

# Fibonacci tail recursively

# Fibonacci stream
