# 1. Nonlocals
# the nonlocal keyword can be used to modify a variable in the parent frame
# outside the current frame.
def stepper(num):
	def step():
		nonlocal num	# declare num as a nonlocal variable
		num += 1		# modify num in the stepper frame
		return num
	return step

# Q1.3 
# Write a function that takes in a value x and updates and prints the result
# based on input functions.
def memory(n):
	"""
	>>> f = memory(10)
	>>> f = f(lambda x: x * 2)
	20
	>>> f = f(lambda x: x - 7)
	13
	>>> f = f(lambda x: x > 5)
	True
	"""
	def update(f):
		nonlocal n
		n = f(n)
		print(n)
		return update

	return update

# 2. Mutable Lists
# Q2.2 Write a function that takes in a value x, a value el, and a list and
# adds as many el's to the end of the list as there are x's. Make sure to
# modify the original list using list mutation techniques.
def add_this_many(x, el, lst):
	"""Adds el to the end of lst the number of times x occurs in lst.
	>>> lst = [1, 2, 4, 2, 1]
	>>> add_this_many(1, 5, lst)
	>>> lst
	[1, 2, 4, 2, 1, 5, 5]
	>>> add_this_many(2, 2, lst)
	>>> lst
	[1, 2, 4, 2, 1, 5, 5, 2, 2]
	"""
	# cnt = 0
	# for num in lst:
	# 	if num == x:
	# 		cnt += 1

	count = sum([1 for num in lst if num == x]) # 这个list comprehension等价于上面的for循环
	for _ in range(count):
		lst.append(el)


# Q2.3 Write a function that takes in a list and reverses it inplace, i.e.
# mutate the given list itself, instead of returning a new list.
def reverse(lst):
	"""Reverses lst in place.
	>>> x = [3, 2, 4, 5, 1]
	>>> reverse(x)
	>>> x
	[1, 5, 4, 2, 3]
	"""
	length = len(lst)
	for k in range(length//2):
		lst[k], lst[length-k-1] = lst[length-k-1], lst[k]

# 3. Dictionaries
# Q3.2 Write a function that takes in a sequence s and a function fn and 
# returns a dictionary. The values of the dictionary are lists of elements
# from s. Each elements e in a list should be constructed such that fn(e)
# is the same for all elements in that list. Finally, the key for each
# value should be fn(3).
def group_by(s, fn):
	"""
	>>> group_by([12, 23, 14, 45], lambda p: p // 10)
	{1: [12, 14], 2: [23], 4: [45]}
	>>> group_by(range(-3, 4), lambda x: x * x)
	{9: [-3, 3], 4: [-2, 2], 1: [-1, 1], 0: [0]}
	"""
	group_dict = {}
	for e in s:
		if fn(e) not in group_dict:
			group_dict[fn(e)] = []
		group_dict[fn(e)].append(e)

	# 下面的代码要for循环两次(之前写的)，lab05的Q6和这题是一样的
	# group_dict = dict([(fn(e), []) for e in s])
	# for e in s:
	# 	group_dict[fn(e)].append(e)
	return group_dict

# Q3.3 Write a function that takes in a deep dictionary d and replace all
# occurences of x as a value (not a key) with y.
# Hint: You will need to combine iteration and recursion. Also, for a 
# dictionary z, type(z) == dict will evaluate to True.
def replace_all_deep(d, x, y):
	"""
	>>> d = {1: {2: 'x', 'x': 4}, 2: {4: 4, 5: 'x'}}
	>>> replace_all_deep(d, 'x', 'y')
	>>> d
	{1: {2: 'y', 'x': 4}, 2: {4: 4, 5: 'y'}}
	"""
	for key, value in d.items():
		if type(value) == dict:
			replace_all_deep(value, x, y)
		if value == x:
			d[key] = y 
