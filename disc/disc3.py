# Trees

# constructor
def tree(label, branches=[]):
	for branch in branches:
		assert is_tree(branch)
	return [label] + list(branches)

# selectors
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

# Example tree construction
t = tree(1,
		[tree(3, 
			[tree(4),
			 tree(5),
			 tree(6)]),
		tree(2)])

t2 = tree(6,
		[tree(5,
			[tree(3),
			 tree(2)]),
		 tree(4,
		 	[tree(1)])])
# Q3.1 Write a function that return the largest number in a tree
def tree_max(t):
	"""Return the max of a tree."""
	if is_leaf(t):
		return label(t)
	else:
		return max([label(t)] + [tree_max(b) for b in branches(t)])

# Q3.2 Write a function that returns the height of a tree. Recall that 
# height of a tree is the length of the longest path from the root to 
# a leaf.
def height(t):
	"""Return the height of a tree."""
	if is_leaf(t):
		return 0
	else:
		return 1 + max([height(b) for b in branches(t)])

# Q3.3 Write a function that takes in a tree and squares every value.
# It should return a new tree. You can assume that every item is a number.
def square_tree(t):
	"""Return a tree with the square of every element in t."""
	return tree(label(t) ** 2, [square_tree(b) for b in branches(t)])

# Q3.4 Write a function that takes in a tree and a value x and returns 
# a list containing the nodes along the path required to get from the root
# of the tree to a node containing x.
# If x is not present in the tree, return None. Assume that the entries of the 
# tree are unique.
t3 = tree(2, 
		[tree(7, 
			[tree(3), 
			 tree(6, 
			 	[tree(5), tree(11)])]),
		 tree(15)])
def find_path(tree, x):
	"""
	>>> find_path(t3, 5)
	[2, 7, 6, 5]
	>>> find_path(t3, 10) # returns None
	"""
	if label(tree) == x:
		return [x]
	for path in [find_path(b, x) for b in branches(tree)]:
		if path:
			return [label(tree)] + path 

# Q3.5 Write a function that takes in a tree and a depth k and returns a 
# new tree that contains only the first k levels of the original tree.
def prune(t, k):
	"""
	>>> prune(t3, 2)
	[2, [7, [3], [6]], [15]]
	"""
	if k == 0:
		return tree(label(t))
	else:
		return tree(label(t), [prune(b, k-1) for b in branches(t)])




