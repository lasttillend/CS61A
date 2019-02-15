"""
Calculate Taylor expansion of sinx.
"""

from math import factorial, sin, pow

def summation(n, x, term):
	""" 
	sum up to nth term.
	"""
	total, k = 0, 1
	while k <= n:
		total, k = total + term(k, x), k + 1
	return total

def sin_term(k, x):
	"""
	the kth term of sinx in its Taylor expansion
	"""
	return pow(-1, k-1) / factorial(2*k-1) * pow(x, 2*k-1)

def sin_taylor_expansion(n, x):
	"""
	approximate sinx by its nth-order Taylor polynomial
	"""
	return summation(n, x, sin_term)


x = sin_taylor_expansion(10, 1)
print(x)
print(sin(1))