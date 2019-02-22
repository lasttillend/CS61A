# Spring2017 Midterm 2 (错题集)

# 5

class Wrinkles:
    """An object that contains a sequence of items and a predicate (true/false function) and that, when iterated over, produces adjacent pairs of items in the sequence that satisfy the predicate.
    >>> w = Wrinkles([1, 2, 3, 2, 4, 8, 5, 4], lambda x, y: x > y)
    >>> for p in w:
    ...     print(p)
    (3, 2)
    (8, 5)
    (5, 4)
    """

    def __init__(self, L, wrinkle):
        self._L = L
        self._wrinkle = wrinkle
        # self.i = 0  # iterator version

    # generator version
    def __iter__(self):
        for k in range(1, len(self._L)):
            if self._wrinkle(self._L[k-1], self._L[k]):
                yield (self._L[k-1], self._L[k])


    # # iterator version
    # def __next__(self):
    #     if self.i == len(self._L) - 1:
    #         raise StopIteration
    #     self.i += 1
    #     if self._wrinkle(self._L[self.i-1], self._L[self.i]):
    #         return (self._L[self.i-1], self._L[self.i])
    #     return next(self)

    # def __iter__(self):
    #     return self

print("Problem 5:")
w = Wrinkles([1, 2, 3, 2, 4, 8, 5, 4], lambda x, y: x > y)
for p in w:
    print(p)

# 6

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


def longest_seq(tr):
    """The length of the longest downward sequence of nodes in TR whose labels are consecutive integers.
    >>> t = Tree(1, [Tree(2), Tree(1, [Tree(2, [Tree(3, [Tree(0)])])])])
    >>> longest_seq(t) # 1 -> 2 -> 3
    3
    >>> t = Tree(1)
    >>> longest_seq(t)
    1
    """
    max_len = 1

    def longest(t):
        """Returns longest downward sequence of nodes starting at T whose labels are consecutive integers. Updates max_len to that length, if greater.
        """
        nonlocal max_len
        n = 1
        if not t.is_leaf():
            for b in t.branches:
                L = longest(b)
                if b.label == t.label + 1:
                    n = max(n, L + 1)  # n: longest starting from root t
            max_len = max(n, max_len)  # max_len: longest anywhere
        return n

    longest(t)
    return max_len

print("Problem 6:")
t = Tree(1, [Tree(2), Tree(1, [Tree(2, [Tree(3, [Tree(0)])])])])  # 1->2->3
t2 = Tree(0, [Tree(1, [Tree(0, [Tree(1, [Tree(2)])])])])  # 0->1->2
print(longest_seq(t))
print(longest_seq(t2))


