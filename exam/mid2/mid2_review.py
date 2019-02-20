# Midterm 2 Review

# 1 List Comprehension

def dot_product(lst1, lst2):
    """Compute the dot product of two lists."""
    return sum([x_k * y_k for x_k, y_k in zip(lst1, lst2)])
    # result = 0
    # for x, y in zip(lst1, lst2):
    #     result += x * y
    # return result

s = [1, 2, 3]
t = [4, 5, 6]
print(dot_product(s, t))

lst = [[j for j in range(i + 1)] for i in range(5)]
print(lst)

lst = [[j for j in range(i + 1) if j != 2] for i in range(5)]
print(lst)

def subset_sum(seq, k):
    """
    >>> subset_sum([2, 4, 7, 3], 5)  # 2 + 3 = 5
    True
    >>> subset_sum([1, 9, 5, 7, 3], 2)
    False
    """

    if len(seq) <= 0:
        return False
    elif seq[0] == k:
        return True
    else:
        using_first = subset_sum(seq[1:], k - seq[0])
        without_using_first = subset_sum(seq[1:], k)
        return using_first or without_using_first

print(subset_sum([2, 4, 7, 3], 5))
print(subset_sum([1, 9, 5, 7, 3], 12))
print(subset_sum([2, 4], 0))

# 2 Trees

def tree(label, branches=[]):
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_leaf(tree):
    return not branches(tree)


def is_min_heap(t):
    """min_heap tree: every node's value is less than or equal to
    the values of all its branches.

    >>> t1 = tree(1, [tree(5, [tree(7)]), tree(3, [tree(9), tree(4)]), tree(6)])
    >>> is_min_heap(t1)
    True
    >>> t2 = tree(1, [tree(5, [tree(7)]), tree(3, [tree(9), tree(2)]), tree(6)])
    >>> is_min_heap(t2)
    False
    """
    for b in branches(t):
        if label(t) > label(b) or not is_min_heap(b):
            return False
    return True

    # my solution
    # if is_leaf(t):
    #     return True
    # else:
    #     branches_min_heap = [is_min_heap(b) for b in branches(t)]
    #     if False in branches_min_heap:
    #         return False
    #     if False in [label(t) <= label(b) for b in branches(t)]:
    #         return False
    #     return True


t1 = tree(1, [tree(5, [tree(7)]), tree(3, [tree(9), tree(4)]), tree(6)])
print(is_min_heap(t1))
t2 = tree(1, [tree(5, [tree(7)]), tree(3, [tree(9), tree(2)]), tree(6)])
print(is_min_heap(t2))

# OOP

class Plant:

    def __init__(self):
        self.leaf = Leaf(self)
        self.materials = []
        self.height = 1

    def absorb(self):
        self.leaf.absorb()

    def grow(self):
        for sugar in self.materials:
            sugar.activate()
            self.height += 1


class Leaf:

    def __init__(self, plant):
        self.alive = True
        self.sugars_used = 0
        self.plant = plant

    def absorb(self):
        if self.alive:
            self.plant.materials.append(Sugar(self, self.plant))

    def __repr__(self):
        return 'Leaf'


class Sugar:
    sugars_created = 0

    def __init__(self, leaf, plant):
        self.leaf = leaf
        self.plant = plant
        Sugar.sugars_created += 1

    def activate(self):
        self.leaf.sugars_used += 1
        self.plant.materials.remove(self)

    def __repr__(self):
        return 'Sugar'

# Extra Practice

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

    def __eq__(self, other):
        return type(other) is type(self) and self.label == other.label \
               and self.branches == other.branches

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

    def copy_tree(self):
        return Tree(self.label, [b.copy_tree() for b in self.branches])


def is_binary(t):
    def binary(t, lo, hi):
        if lo < t.label < hi:
            if t.is_leaf():
                return True
            elif len(t.branches) == 1 and t.branches[0].label < t.label:
                return binary(t.branches[0], lo, t.label)
            elif len(t.branches) == 2 and t.branches[0].label < t.label < t.branches[1].label:
                return binary(t.branches[0], lo, t.label) and binary(t.branches[1], t.label, hi)
        return False
    return binary(t, float('-inf'), float('inf'))


t1 = Tree(5, [Tree(3, [Tree(2), Tree(4)]), Tree(8, [Tree(7), Tree(10, [Tree(9)])])])
print(is_binary(t1))
t2 = Tree(5, [Tree(8, [Tree(1), Tree(10)]), Tree(9)])
print(is_binary(t2))
t3 = Tree(5, [Tree(1), Tree(6), Tree(7)])
print(is_binary(t3))
t4 = Tree(1)
print(is_binary(t4))





