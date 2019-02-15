# Lists
# 1. Translating a List Diagram to Code
# DO NOT use numerals or mathmatical operators
x, y, z = 1, 2, 3
y = [x, [y, [z, []]]]
x = [y[1][0], y, [[]]]
z = len([])

# Tree Recursion
# 1. Tree Recursion with Trees
def sum_range(t):
	"""Returns the range of the sums of t, that is, the difference between
	   the largest and the smallest sums of t."""
	def helper(t):
		if is_leaf(t):
			return [label(t), label(t)]
		else:
			a = min([helper(b)[1] for b in branches(t)])
			b = max([helper(b)[0] for b in branches(t)])
			x = label(t)
			return [b + x, a + x] # 储存每个branch的max/min

	x, y = helper(t)
	return x - y

# 2. This One Goes to Eleven
def no_eleven(n):
	"""Return a list of lists of 1's and 6's that do not contain 1 after 1."""
	if n == 0:
		return [[]]
	elif n == 1:
		return [[1], [6]]
	else:
		a, b = no_eleven(n - 2), no_eleven(n - 1)
		return [s + [6, 1] for s in a] + [s + [6] for s in b]

# 3. Expression Trees
def eval_with_add(t):
	"""Evaluate an expression tree of * and + using only addition.
	>>> plus = tree('+', [tree(2), tree(3)])
	>>> eval_with_add(plus)
	5
	>>> times = tree('*', [tree(2), tree(3)])
	>>> eval_with_add(times)
	6
	>>> deep = tree('*', [tree(2), plus, times])
	>>> eval_with_add(deep)
	60
	>>> eval_with_add(tree('*'))
	1
	"""
	if label(t) == '+':
		return sum([eval_with_add(b) for b in branches(t)])
	elif label(t) == '*':
		total = 1
		for b in branches(t):
			total, term = 0, total
			for _ in range(eval_with_add(b)):
				total = total + term
		return total
	else:
		return label(t)

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