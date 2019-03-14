# OOP Trees and Linked Lists

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


class Link:
    """A linked list with a first element and the rest."""
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

### 1 OOP
# 1. Linky Path
def linky_paths(t):
    """
    >>> t = Tree(1, [Tree(2)])
    >>> linky_paths(t)
    >>> t
    Tree(Link(1), [Tree(Link(2, Link(1)))])
    """
    def helper(t, path_so_far):
        t.label = Link(t.label, path_so_far)
        for b in t.branches:
            helper(b, t.label)
    helper(t, Link.empty)

t = Tree(1, [Tree(2, [Tree(5), Tree(6)]), Tree(3), Tree(4)])
print(t)
linky_paths(t)
print(t)

# 2. Find File Path
def find_file_path(t, file_str):
    """
    >>> t = Tree('data', [Tree('comm', [Tree('dummy.py')]), Tree('ecc', [Tree('hello.py'), Tree('file.py')]), Tree('file2.py')])
    >>> find_file_path(t, 'file2.py')
    '/data/file2.py'
    >>> find_file_path(t, 'dummy.py')
    '/data/comm/dummy.py'
    >>> find_file_path(t, 'hello.py')
    '/data/ecc/hello.py'
    >>> find_file_path(t, 'file.py')
    '/data/ecc/file.py'
    """
    def helper(t, file_str, path_so_far):
        if t.label == file_str:
            return path_so_far + '/' + file_str
        elif t.is_leaf():
            return
        for b in t.branches:
            result = helper(b, file_str, path_so_far + '/' + t.label)
            if result is not None:
                return result
    return helper(t, file_str, '')

t = Tree('data', [Tree('comm', [Tree('dummy.py')]), Tree('ecc', [Tree('hello.py'), Tree('file.py')]), Tree('file2.py')])

### 2 Linked Lists
# 1. Convert to String
def convert_to_string(link):
    """
    >>> link = Link('data', Link('file2.py'))
    >>> convert_to_string(link)
    '/data/file2.py'
    """
    if link is Link.empty:
        return ''
    return '/' + link.first + convert_to_string(link.rest)

# 2. All Paths Linked
def all_paths_linked(t):
    """
    >>> t1 = Tree(1, [Tree(2), Tree(3)])
    >>> t2 = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)])])
    >>> all_paths_linked(t1)
    [Link(1, Link(2)), Link(1, Link(3))]
    >>> all_paths_linked(t2)
    [Link(1, Link(2)), Link(1, Link(3, Link(4))), Link(1, Link(3, Link(5)))]
    """

    if t.is_leaf():
        return [Link(t.label)]
    result = []
    for branch in t.branches:
        result = result + [Link(t.label, p) for p in all_paths_linked(branch)]
    return result

# 3. Find File Path 2
def find_file_path2(t, file_str):
    """
    >>> t = Tree('data', [Tree('comm', [Tree('dummy.py')]), Tree('ecc', [Tree('hello.py'), Tree('file.py')]), Tree('file2.py')])
    >>> find_file_path2(t, 'file2.py')
    '/data/file2.py'
    >>> find_file_path2(t, 'dummy.py')
    '/data/comm/dummy.py'
    >>> find_file_path2(t, 'hello.py')
    '/data/ecc/hello.py'
    >>> find_file_path2(t, 'file.py')
    '/data/ecc/file.py'
    """
    for link in all_paths_linked(t):
        original = ''
        while link is not Link.empty:
            if link.first == file_str:
                return original + '/' + file_str
            link, original = link.rest, original + '/' + link.first

# 4. Skip
def skip(lnk, n):
    """
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    >>> skip(lnk, 2)
    >>> lnk
    Link(1, Link(3, Link(5)))
    >>> lnk2 = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    >>> skip(lnk2, 4)
    >>> lnk2
    Link(1, Link(2, Link(3, Link(5, Link(6)))))
    """
    count = 0
    def skipper(lst):
        nonlocal count
        count += 1
        if lst is Link.empty:
            return
        elif (count + 1) % n == 0:
            lst.rest = lst.rest.rest
            count = 0
        skipper(lst.rest)
    skipper(lnk)

