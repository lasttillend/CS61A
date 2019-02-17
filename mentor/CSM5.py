# Computer Science Mentors 5: Linked Lists and Midterm Review

# Linked Lists
class Link:
	"""A linked list with a first element and the rest."""
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

	def __getitem__(self, i):
		if i == 0:
			return self.first
		else:
			return self.rest[i-1]

	def __len__(self):
		return 1 + len(self.rest)

	def __repr__(self):
		if self.rest:
			rest_str = ', ' + repr(self.rest)
		else:
			rest_str = ''
		return 'Link({0}{1})'.format(self.first, rest_str)
		
	def __str__(self):
		string = '<'
		while self.rest is not Link.empty:
			string += str(self.first) + ' '
			self = self.rest
		return string + str(self.first) + '>'

# 2 
def skip(lst): 
	"""
	Returns a new Link with every other element skipped.

	>>> a = Link(1, Link(2, Link(3, Link(4))))
	>>> a
	Link(1, Link(2, Link(3, Link(4))))
	>>> b = skip(a)
	>>> b
	Link(1, Link(3))
	>>> a
	Link(1, Link(2, Link(3, Link(4))))
	"""
	if lst is Link.empty:
		return Link.empty
	elif lst.rest is Link.empty:
		return Link(lst.first) 
	else:
		return Link(lst.first, skip(lst.rest.rest))

# 3
def skip2(lst):
	"""
	Mutating the original list
	>>> a = Link(1, Link(2, Link(3, Link(4))))
	>>> b = skip2(a)
	>>> b
	>>> a
	Link(1, Link(3))
	"""
	if lst is Link.empty or lst.rest is Link.empty:
		return None
	skip2(lst.rest.rest)	
	lst.rest = lst.rest.rest
	
# 4 
def reverse(lst):
	"""
	>>> a = Link(1, Link(2, Link(3)))
	>>> b = reverse(a)
	>>> b
	Link(3, Link(2, Link(1)))
	>>> a
	Link(1, Link(2, Link(3)))
	"""
	def reverse_link_helper(prev, rest):
		if prev is Link.empty:
			return rest
		else:
			return reverse_link_helper(prev.rest, Link(prev.first, rest))

	return reverse_link_helper(lst, Link.empty)

### Midterm Review ###
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

# 1
def contains_n(elem, n, t):
	"""
	>>> t1 = Tree(1, [Tree(1, [Tree(2)])])
	>>> contains_n(1, 2, t1)
	True
	>>> contains_n(2, 2, t1)
	False
	>>> contains_n(2, 1, t1)
	True
	>>> t2 = Tree(1, [Tree(2), Tree(1, [Tree(1), Tree(2)])])
	>>> contains_n(1, 3, t2)
	True
	>>> contains_n(2, 2, t2)
	False
	>>> t3 = Tree(1, [Tree(1, [Tree(2, [Tree(1), Tree(3, [Tree(2)])])]), Tree(2, [Tree(5), Tree(3)]), Tree(4)])
	"""
	if n == 0:
		return True
	elif n == 1 and t.is_leaf():
		return t.label == elem  
	elif t.label == elem:
		return True in [contains_n(elem, n - 1, b) for b in t.branches]
	else:
		return True in [contains_n(elem, n, b) for b in t.branches]

# 2
def factor_tree(n):
	for i in range(2, n):
		if n % i == 0:
			return Tree(n, [Tree(i), factor_tree(n // i)])
	return Tree(n)

