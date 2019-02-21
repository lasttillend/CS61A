# Recursive Data Structure and Orders of Growth

# 1 Linked Lists

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ", " + repr(self.rest)
        return "Link({0}{1})".format(self.first, rest)


five_links = Link(1, Link(2, Link(3, Link(4, Link(5)))))
ten_links = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6, Link(7, Link(8, Link(9, Link(10))))))))))

# (a)
print("1 Linked Lists")
print("Problem (a):")
def rotate_left(lnk):
    """
    >>> rotate_left(five_links)
    Link(2, Link(3, Link(4, Link(5, Link(1)))))
    """
    if lnk.rest is Link.empty:
        return lnk
    second = lnk.rest
    current = lnk
    while current.rest is not Link.empty:
        current = current.rest
    current.rest = lnk
    lnk.rest = Link.empty
    return second


print(rotate_left(five_links))

# (b)
def rotate_right(lnk):
    if lnk.rest is Link.empty:
        return lnk
    previous = lnk
    current = lnk.rest
    while current.rest is not Link.empty:
        previous = previous.rest
        current = current.rest
    current.rest = lnk
    previous.rest = Link.empty
    return current


print("Problem(b):")
five_links = Link(1, Link(2, Link(3, Link(4, Link(5)))))
print(rotate_right(five_links))

# (c)
def filter_links(lnk, pred):
    """
    >>> filter_links(ten_links, lambda x: x % 3 == 0)
    Link(3, Link(6, Link(9)))
    >>> ten_links  # not changed!
    Link(1, Link(2, Link(3, Link(4, Link(5, Link(6, Link(7, Link(8, Link(9, Link(10))))))))))
    """
    if lnk is Link.empty:
        return Link.empty
    elif pred(lnk.first):
        return Link(lnk.first, filter_links(lnk.rest, pred))
    else:
        return filter_links(lnk.rest, pred)

print("Problem(c):")
print(filter_links(ten_links, lambda x: x ** 2 < 10))
print(ten_links)

# (d)
def length(lnk):
    if lnk is Link.empty:
        return 0
    else:
        return 1 + length(lnk.rest)

def delete_every_k(lnk, k):
    if length(lnk) < k:
        return
    current = lnk
    for _ in range(k - 2):
        current = current.rest
    # Delete the item after current
    delete_every_k(current.rest.rest, k)
    current.rest = current.rest.rest

print("Problem(d):")
delete_every_k(ten_links, 4)
print(ten_links)

# 2 Trees

class Tree:

    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return len(self.branches) == 0

    def __repr__(self):
        if self.branches:
            return "Tree({0}, {1})".format(self.label, repr(self.branches))
        else:
            return "Tree({0})".format(repr(self.label))

# (a)
print("2 Trees")
print("Problem(a):")

def is_prime(n):
    """Returns True if n is a prime number and False otherwise."""
    def calculate(k):
        if k <= n ** 0.5:
            if n % k == 0:
                return False
            else:
                return calculate(k + 1)
        else:
            return True

    return calculate(2)


def prime_factors_tree(n):
    if is_prime(n):
        return Tree(n)
    k = 2
    while n % k != 0:
        k += 1
    return Tree(n, [prime_factors_tree(n // k) ,Tree(k)])

print(prime_factors_tree(3))
print(prime_factors_tree(12))
print(prime_factors_tree(100))
print(prime_factors_tree(168))

# (b)
print("Problem(b):")
def get_leaves(t):
    if t.is_leaf():
        return [t.label]
    else:
        return sum([get_leaves(b) for b in t.branches],[])

print(get_leaves(prime_factors_tree(3)))
print(get_leaves(prime_factors_tree(12)))
print(get_leaves(prime_factors_tree(100)))
print(get_leaves(prime_factors_tree(168)))
