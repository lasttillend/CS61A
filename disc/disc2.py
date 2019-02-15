"""	Question1: I want to go up a flight of stairs that has n steps. I can
	either take 1 or 2 steps each time. How many different ways can I go 
	up this flight of stairs? Write a function count_stair_ways that solves
	this problem for me. Assume n is positive.
"""

def count_stair_ways(n):
	"""return the number of ways to go up stairs using 1 or 2 steps each time. 

	n: length of stairs, positive integer

	>>> count_stair_ways(1)
	1
	>>> count_stair_ways(2)
	2
	>>> count_stair_ways(3)
	3
	>>> count_stair_ways(5)
	8
	"""
	assert n > 0 and n == int(n), "n must be a positive integer."
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return count_stair_ways(n - 1) + count_stair_ways(n - 2)


"""	Question2: Consider a special version of the count_stairways problem,
	where instead of 1 or 2 steps, we are able take up to and including k
	steps at a time. 
	Write a function count_k that figures out the number of paths for this
	scenario. Assume n and k are positive.
"""

def count_k(n, k):
	"""return the number of ways to go up stairs using up to k steps each time.

	n: length of stairs, positive integer
	k: longest step, positive integer

	>>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
	4
	>>> count_k(4, 4) 
	8
	>>> count_k(10, 3)
	274
	>>> count_k(300, 1) # only one step at a time
	1
	"""
	if n == 0:
		return 1
	elif n < 0:
		return 0
	else:
		total, i = 0, 1
		while i <= k:
			total += count_k(n - i, k)
			i += 1
		return total



