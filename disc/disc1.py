""" Discussion 1 """


# Q1.1
def wears_jacket(temp, raining):
	return temp < 60 or raining

# Q1.2
def handle_overflow(s1, s2):
	if s1 <= 30 and s2 <= 30:
		print("No overflow")
	else:
		if s1 >= 30 and s2 >= 30:
			print("No space left in either section")
		elif s1 < 30:
			print("Move to section 1: ", 30 - s1)
		elif s2 < 30:
			print("Move to section 2: ", 30 - s2)

	

# Q1.3
def square(x):
	return x * x

def so_slow(num):
	x = num
	while x > 0:
		x = x + 1 # infinite loop 
	return x / 0

# Q1.4
from math import sqrt
def is_prime(n):
	"""
	>>> is_prime(10)
	False
	>>> is_prime(7)
	True
	"""
	assert n >= 1, "n is not a positive integer"
	k = 2
	if n == 1:
		flag = False
	else:
		flag = True
	while k <= sqrt(n):
		if n % k == 0:
			flag = False
			break
		k += 1
	return flag

# Q2.1
def keep_ints(cond, n):
	"""Print out all integers 1..i..n where cond(i) is true

	>>> def is_even(x):
	...		# Even numbers have remainder 0 when divided by 2.
	...		return x % 2 == 0
	>>> keep_ints(is_even, 5)
	2
	4
	"""
	i = 1
	while i <= n:
		if cond(i):
			print(i)
		i += 1


# Q2.2
def outer(n):
	def inner(m):
		return n - m
	return inner

# Q2.3
def keep_ints(n):
	"""Returns a function which takes one parameter cond and 
	prints out all integers 1..i..n where calling cond(i) returns True.

	>>> def is_even(x):
	...     # Even numbers have remainder 0 when divided by 2.
	...     return x % 2 == 0
	>>> keep_ints(5)(is_even)
	2
	4
	"""
	def f(cond):
		i = 1
		while i <= n:
			if cond(i):
				print(i)
			i += 1
	return f




