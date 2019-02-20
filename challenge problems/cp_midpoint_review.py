# Midpoint Review

# 1 Recursion

# (a)
def parens(n):
    """
    >>> parens(2)
    ["()()", "(())"]
    >>> parens(3)
    ["()()()", "()(())", "(())()", "(()())", "((()))"]
    """
    if n < 1:
        return ""
    elif n == 1:
        return ["()"]
    else:
        parens_one_fewer = parens(n - 1)
        not_deeper = (["(){}".format(p) for p in parens_one_fewer]  # 始终加"()"到左边
                    + ["{}()".format(p) for p in parens_one_fewer if "{}()".format(p) != "(){}".format(p)]) # 只有会产生不同的情况时才加到右边
        deeper = ["({})".format(p) for p in parens_one_fewer]
        return not_deeper + deeper

print("1 Recursion")
print("Problem (a):")
print(parens(3))

# (b)
def insert_char(s, char, idx):
    return s[:idx] + str(char) + s[idx:]


def perms(s):
    if len(s) <= 0:
        return []
    elif len(s) == 1:
        return [s]
    else:
        perms_one_fewer = perms(s[1:])
        return [insert_char(p, s[0], k) for p in perms_one_fewer for k in range(len(p) + 1)]

print("Problem (b):")
print(perms('61a'))

# (c)
def climb(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climb(n - 1) + climb(n - 2)

print("Problem (c):")
print(climb(3))

# (d)
def pascal(i, j):
    if j == 0 or j == i:
        return 1
    else:
        return pascal(i - 1, j - 1) + pascal(i - 1, j)

print("Problem (d):")
print(pascal(4, 0))
print(pascal(4, 2))
print(pascal(4, 3))
print(pascal(5, 3))


# 2 Mutable Data and Functions

# (b) theta(n): first time called on n; theta(1): later calls on n
def fast_fib():
    memo = {}
    def fib(n):
        if n in memo:
            return memo[n]
        else:
            prev = 0
            current = 1
            for _ in range(n):
                prev, current = current, prev + current
            memo[n] = current
        return current
    return fib


print("2 Mutable Data and Functions")
print("Problem (b)")
fib = fast_fib()
print(fib(7))


# 3 Hierarchical Data Structure

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            rest = ""
        else:
            rest = ", " + repr(self.rest)
        return "Link({0}{1})".format(self.first, rest)


# (a)
def reverse_print(lnk):
    if lnk is Link.empty:
        return
    reverse_print(lnk.rest)
    print(lnk.first)

print("3 Hierarchical Data Structure")
print("Problem(a):")
s = Link(1, Link(2, Link(3, Link(4, Link(5)))))
reverse_print(s)
print(s) # s is not changed

# (b) theta(n) time: n is the length of the list
def k_from_end(lnk, k):
    """Returns the kth element from the end of a linked list.

    >>> k_from_end(Link(1, Link(2, Link(3, Link(4)))), 2)
    2
    """
    tortise, hare = lnk, lnk
    for _ in range(k):
        hare = hare.rest

    while hare.rest is not Link.empty:
        tortise, hare = tortise.rest, hare.rest
    return tortise.first

print("Problem (b):")
print(k_from_end(Link(1, Link(2, Link(3, Link(4)))), 2))

# (c)
def reverse_k(lnk, k):
    """
    >>> x = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6, Link(7, Link(8, Link(9)))))))))
    >>> y = reverse_k(x, 3)
    >>> y
    Link(3, Link(2, Link(1, Link(6, Link(5, Link(4, Link(9, Link(8, Link(7)))))))))
    """
    if lnk is Link.empty or lnk.rest is Link.empty:
        return lnk
    prev, current = lnk, lnk.rest
    for _ in range(k - 1):
        temp = prev
        prev, current = current, current.rest
        prev.rest = temp
    lnk.rest = reverse_k(current, k)
    return prev


x = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6, Link(7, Link(8, Link(9)))))))))
y = reverse_k(x, 3)
print("Problem(c):")
print(y)
# print(x)  # mutates x

# (d)

class Tree:

    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            return "Tree({0}, {1})".format(self.label, repr(self.branches))
        else:
            return "Tree({0})".format(self.label)


def is_bst(t):
    """Returns whether or not t is a valid binary search tree."""
    def bst_helper(t, lo, hi):
        if t.label < lo or t.label > hi:
            return False
        if t.is_leaf():
            return True
        if len(t.branches) != 2:
            return False
        return bst_helper(t.branches[0], lo, t.label) and bst_helper(t.branches[1], t.label, hi)

    return bst_helper(t, -float("inf"), float("inf"))

print("Problem (d):")
t1 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5)])
t2 = Tree(4, [Tree(2, [Tree(1), Tree(3)]), Tree(6, [Tree(5), Tree(7)])])
print(is_bst(t1))
print(is_bst(t2))


