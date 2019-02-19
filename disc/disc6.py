# Orders of Growth and Linked Lists

# 3 Linked Lists


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.second
    3
    >>> s.first = 5
    >>> s.second = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


def prod(iterable):
    from functools import reduce
    from operator import mul
    return reduce(mul, iterable, 1)
    # if len(lst) == 0:
    #     return 1
    # else:
    #     return lst[0] * prod(lst[1:])

# 3.1


def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest
    ()
    """
    # recursively
    product = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link.empty
        product *= lnk.first
    lst_of_lnks_rest = [lnk.rest for lnk in lst_of_lnks]
    return Link(product, multiply_lnks(lst_of_lnks_rest))

    # # iteratively
    # head = Link.empty
    # tail = head
    # while Link.empty not in lst_of_lnks:
    #     all_prod = prod([lnk.first for lnk in lst_of_lnks])
    #     if head is Link.empty:
    #         head = Link(all_prod)
    #         tail = head
    #     else:
    #         tail.rest = Link(all_prod)
    #         tail = tail.rest
    #     lst_of_lnks = [lnk.rest for lnk in lst_of_lnks]
    # return head


# 3.2
def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> unique = remove_duplicates(lnk)
    >>> unique
    Link(1, Link(5))
    >>> lnk
    Link(1, Link(5))
    """
    # recursively
    if lnk is Link.empty or lnk.rest is Link.empty:
        return lnk
    elif lnk.first == lnk.rest.first:
        lnk.rest = lnk.rest.rest
        remove_duplicates(lnk)
        return lnk
    else:
        remove_duplicates(lnk.rest)
        return lnk

    # # iteratively
    # cur = lnk
    # while cur is not Link.empty and cur.rest is not Link.empty:
    #     if cur.first == cur.rest.first:
    #         cur.rest = cur.rest.rest
    #     else:
    #         cur = cur.rest
    # return lnk

# 4 Midterm Review

# 4.1


def even_weighted(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [idx * lst[idx] for idx in range(len(lst)) if idx % 2 == 0]

# 4.2


def quicksort_list(lst):
    """
    >>> quicksort_list([3, 1, 4])
    [1, 3, 4]
    """
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    less = [x for x in lst if x < pivot]
    greater = [x for x in lst if x > pivot]
    return quicksort_list(less) + [pivot] + quicksort_list(greater)

# 4.3


def max_product(lst):
    """Return the maximum product that can be formed using lst
    without using any consecutive numbers
    >>> max_product([10, 3, 1, 9, 2]) # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(lst) == 0:
        return 1
    elif len(lst) == 1:
        return lst[0]
    else:
        using_first = lst[0] * max_product(lst[2:])
        without_using_first = max_product(lst[1:])
        return max(using_first, without_using_first)

# 4.4


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


def eval_tree(tree):
    """Evaluate an expression tree with functions the root.
    >>> eval_tree(tree(1))
    1
    >>> expr = tree('*', [tree(2), tree(3)])
    >>> eval_tree(expr)
    6
    >>> eval_tree(tree('+', [expr, tree(4), tree(5)]))
    15
    """
    if is_leaf(tree):
        return label(tree)
    args = [eval_tree(b) for b in branches(tree)]
    if label(tree) == '*':
        return prod(args)
    else:  # label(tree) == '+'
        return sum(args)

# 4.5


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


def print_levels(t):
    level = {}  # contains the node at each level

    def get_level(t, depth):
        if depth in level:
            level[depth].append(t.label)
        else:
            level[depth] = [t.label]
        for b in t.branches:
            get_level(b, 1 + depth)

    get_level(t, 0)
    for depth in level:
        print(level[depth])


def redundant_map(t, f):
    """
    >>> double = lambda x: x*2
    >>> tree = Tree(1, [Tree(1), Tree(2, [Tree(1, [Tree(1)])])])
    >>> print_levels(redundant_map(tree, double))
    [2] # 1 * 2 ˆ (1) ; Apply double one time
    [4, 8] # 1 * 2 ˆ (2), 2 * 2 ˆ (2) ; Apply double two times
    [16] # 1 * 2 ˆ (2 ˆ 2) ; Apply double four times
    [256] # 1 * 2 ˆ (2 ˆ 3) ; Apply double eight times
    """
    t.label = f(t.label)

    def new_f(x):
        return f(f(x))
    t.branches = [redundant_map(branch, new_f) for branch in t.branches]
    return t
