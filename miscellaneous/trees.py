def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)

def contains(t, e):
    """Returns True if t contains the element e, and False otherwise."""
    if label(t) == e:
        return True
    for b in branches(t):
        if contains(b, e):
            return True
    return False

def all_paths(t):
    """Returns a list of paths from the root to each leaf.

    >>> t = tree(5, [tree(3, [tree(2), tree(1)]), tree(6)])
    >>> all_paths(t)
    [[5, 3, 2], [5, 3, 1], [5, 6]]
    """
    if is_leaf(t):
        return [[label(t)]]
    paths = []
    for b in branches(t):
        for path in all_paths(b):
            paths.append([label(t)] + path)
    return paths

def max_tree(t):
    """
    >>> t = tree(5, [tree(3, [tree(2), tree(1)]), tree(6)])
    >>> max_tree(t)
    [6, [3, [2], [1]], [6]]
    >>> t1 = tree(5, [tree(3, [tree(2), tree(4)]), tree(6)])
    >>> max_tree(t1)
    [6, [4, [2], [4]], [6]]
    """
    if is_leaf(t):
        return tree(label(t))
    max_branches = [max_tree(b) for b in branches(t)]
    max_node = max([label(t)] + [label(b) for b in max_branches])
    return tree(max_node, max_branches)

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        branch_counts = [count_leaves(b) for b in branches(tree)]
        return sum(branch_counts)


def leaves(tree):
    """Return a list containing the leaf labels of tree.

    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])


def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented."""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        return tree(label(t), [increment_leaves(b) for b in branches(t)])


def increment(t):
    """Return a tree like t but with all labels incremented."""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])  # 如果要修改所有的label, 则不需要专门写一个if statement来说明base   case的情况.因为当没有branch的时候会返回[], and we are done, 不再make any recursive call


def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m."""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n - m, m)
        right = partition_tree(n, m - 1)
        return tree(m, [left, right])

# print_tree(partition_tree(6, 4))


def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)

# print_parts(partition_tree(6, 4))


def right_binarize(t):
    """Construct a right-branching binary tree."""
    return tree(label(t), binarize_branches(branches(t)))


def binarize_branches(bs):
    """Binarize a list of branches."""
    if len(bs) > 2:
        first, rest = bs[0], bs[1:]
        return [right_binarize(first), binarize_branches(rest)]
    else:
        return [right_binarize(b) for b in bs]

# Tree class


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

t = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5)])

def equal(t1, t2):
    """Returns True if t1 and t2 are equal trees.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5)])
    >>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5)])
    >>> print(equal(t1, t2))
    True
    """
    if t1.label != t2.label:
        return False
    elif len(t1.branches) != len(t2.branches):
        return False
    else:
        return all(equal(child1, child2) for child1, child2 in zip(t1.branches, t2.branches))
        # for b1, b2 in zip(t1.branches, t2.branches):
        #     if not equal(b1, b2):
        #         return False
        # return True

def size(t):
    """Returns the number of elements in a tree.

    >>> t1 = Tree(1,
                    [Tree(2, [Tree(4)]),
                     Tree(3)])
    >>> size(t1)
    4
    """
    return 1 + sum([size(b) for b in t.branches])

def height(t):
    """Returns the height of the tree.

    >>> leaf = Tree(1)
    >>> height(leaf)
    0
    >>> t1 = Tree(1,
                    [Tree(2, [Tree(4)]),
                     Tree(3)])
    >>> height(t1)
    2
    """
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in t.branches])

def same_shape(t1, t2):
    """Returns True if t1 and t2 have the same structure, but not necessarily the same entries.
    """
    if len(t1.branches) != len(t2.branches):
        return False
    else:
        return all([same_shape(child1, child2) for child1, child2 in zip(t1.branches, t2.branches)])

def sprout_leaves(t, vals):
    """For every leaf of the tree t, mutate it so that it has a list of branches where the items are the elements in the list of values.
    """
    if t.is_leaf():
        t.branches = [Tree(new_leaf) for new_leaf in vals]
    else:
        for b in t.branches:
            sprout_leaves(b, vals)

def prune_leaves(t, vals):
    """For every leaf of the tree t, remove it if its entry is in the list of values.
    """
    if t.is_leaf():
        if t.label not in vals:
            return t
        else:
            return None
    new_branches = [prune_leaves(b, vals) for b in t.branches]
    t.branches = [b for b in new_branches if b is not None]
    return t

