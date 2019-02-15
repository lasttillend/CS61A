# Computer Science Mentors 3
# Mutation and Nonlocal

# Mutation
# 3. Given some list lst, possibly a deep list, mutable lst to have the 
# accumulated sum of all elements so far in the list. If there is a nested
# list, mutate it to similarity reflect the accumulated sum of all elements
# so far in the nested list. Return the total sum of lst.
# Hint: the isinstance function returns True for isinstance(l, list) if l
# is a list and False otherwise.
def accumulate(lst):
	"""
	>>> l = [1, 5, 13, 4]
	>>> accumulate(l)
	23
	>>> l
	[1, 6, 19, 23]
	>>> deep_l = [3, 7, [2, 5, 6], 9]
	>>> accumulate(deep_l)
	32
	>>> deep_l
	[3, 10, [2, 7, 13], 32]
	"""
	total = 0
	for i in range(len(lst)):
		el = lst[i]
		if isinstance(el, list):
			inside = accumulate(el)
			total += inside
		else:
			total += lst[i]
			lst[i] = total
	return total

# Nonlocality
# 2. Pingpong again...
def has_seven(k): # Use this function for your answer below
	if k % 10 == 7:
		return True
	elif k < 10:
		return False
	else:
		return has_seven(k // 10)

def make_pingpong_tracker():
	"""Returns a function that returns the next value in the pingpong
	sequence each time it is called.
	>>> output = []
	>>> x = make_pingpong_tracker()
	>>> for _ in range(9):
	... output += [x()]
	>>> output 
	[1, 2, 3, 4, 5, 6, 7, 6, 5]
	"""
	index, current, add = 1, 0, True
	def pingpong_tracker():
		nonlocal index, current, add
		if add:
			current += 1
		else:
			current -= 1
		if has_seven(index) or index % 7 == 0:
			add = not add
		index += 1
		return current

	return pingpong_tracker