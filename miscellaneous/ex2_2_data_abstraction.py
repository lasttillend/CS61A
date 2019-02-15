# 2.2.1 Example: Rational Numbers

# manapulating rational numbers
def add_rationals(x, y):
	nx, dx = numer(x), denom(x)
	ny, dy = numer(y), denom(y)
	return rational(nx * dy + ny * dx, dx * dy)

def mul_rationals(x, y):
	return rational(numer(x) * numer(y), denom(x) * denom(y))

def print_rational(x):
	print(numer(x), '/', denom(x))

def rationals_are_equal(x, y):
	return numer(x) * denom(y) == numer(y) * denom(x)

# representing rational numbers
from fractions import gcd
def rational(n, d):
	g = gcd(n, d)
	return [n//g, d//g]

def numer(x):
	return x[0]

def denom(x):
	return x[1]



