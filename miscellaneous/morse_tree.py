# Morse Tree

# Key Concepts:
# 1. Branches are list of trees. If you want to traverse through a tree, then you can consider each branch, find the one you are looking for and use that as your remaining tree.
# 2. Building up a tree incrementally by traversing through the tree while appending branches at the same time.

# Link & Tree

class Link:
    """A linked list."""
    empty=()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

class Tree:
    """A tree with label as its label value."""
    def __init__(self, label, branches=()):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches

from io import StringIO
# A StringIO is a file-like object that builds a string instead of printing
# anything out.

def height(tree):
    """The height of a tree."""
    if tree.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in tree.branches])

def width(tree):
    """Returns the printed width of this tree."""
    label_width = len(str(tree.label))
    w = max(label_width,
            sum([width(t) for t in tree.branches]) + len(tree.branches) - 1)
    extra = (w - label_width) % 2
    return w + extra

def pretty(tree):
    """Print a tree laid out horizontally rather than vertically."""

    def gen_levels(tr):
        w = width(tr)
        label = str(tr.label)
        label_pad = " " * ((w - len(label)) // 2)
        yield w
        print(label_pad, file=out, end="")
        print(label, file=out, end="")
        print(label_pad, file=out, end="")
        yield

        if tr.is_leaf():
            pad = " " * w
            while True:
                print(pad, file=out, end="")
                yield
        below = [ gen_levels(b) for b in tr.branches ]
        L = 0
        for g in below:
            if L > 0:
                print(" ", end="", file=out)
                L += 1
            w1 = next(g)
            left = (w1-1) // 2
            right = w1 - left - 1
            mid = L + left
            print(" " * left, end="", file=out)
            if mid*2 + 1 == w:
                print("|", end="", file=out)
            elif mid*2 > w:
                print("\\", end="", file=out)
            else:
                print("/", end="", file=out)
            print(" " * right, end="", file=out)
            L += w1
        print(" " * (w - L), end="", file=out)
        yield
        while True:
            started = False
            for g in below:
                if started:
                    print(" ", end="", file=out)
                next(g);
                started = True
            print(" " * (w - L), end="", file=out)
            yield

    out = StringIO()
    h = height(tree)
    g = gen_levels(tree)
    next(g)
    for i in range(2*h + 1):
        next(g)
        print(file=out)
    print(out.getvalue(), end="")

# Morse Tree

abcde = {'a': '._', 'b': '_...', 'c': '_._.', 'd': '_..', 'e': '.'}

def morse(code):
    """Return a tree representing the code. Each internal (non-leaf) node
    of the tree other than its root is a signal. Each leaf node
    is a letter encoded by the path from the root.

    >>> pretty(morse(abcde))
       None
     /    \
     .    -
    / \   |
    - e   .
    |    /  \
    a    .  -
        / \ |
        . d .
        |   |
        b   c
    """
    root = Tree(None)
    for letter, signals in sorted(code.items()):
        t = root  # back to the root each time a new signals comes in
        for signal in signals:  # trace through tree t
            match = [b for b in t.branches if b.label == signal]
            if match:  # if signal already exists, change t to be that branch
                assert len(match) == 1
                t = match[0]
            else:  # creates a new branch for signal if not exists, then traverse down t
                branch = Tree(signal)
                t.branches.append(branch)
                t = branch
        t.branches.append(Tree(letter))  # add the leaf for letter
    return root

pretty(morse(abcde))

def decode(signals, tree):
    """Decode signals into a letter according to tree, assuming signals
    correctly represents a letter.  tree has the format returned by
    morse().

    >>> t = morse(abcde)
    >>> [decode(s, t) for s in ['-..', '.', '-.-.', '.-', '-..', '.']]
    ['d', 'e', 'c', 'a', 'd', 'e']
    """
    for signal in signals:  # select a branch that matches the signal each time
        tree = [b for b in tree.branches if b.label == signal][0]  # the tree that morse creates should have branches whose labels are signals dot or dash.
    leaves = [b for b in tree.branches if b.is_leaf()]  # this subtree is supposed to have exactly one leaf
    assert len(leaves) == 1
    return leaves[0].label

t = morse(abcde)
print([decode(s, t) for s in ['_..', '.', '_._.', '._', '_..', '.']])

