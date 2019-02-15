from math import exp

def summation(n, term):
	"""Return the sum of n terms."""
	"""Return the sum of the first n terms in a sequence.
	n 		-- a positive integer
	term 	-- a function that takes one argument.
	"""
	total, k = 0, 1
	while k <= n:
		total += term(k)
		k += 1
	return total

def product(n, term):
	"""Return the product of the first n terms in a sequence.
    n    -- a positive integer
    term -- a function that takes one argument
    """
	total, k = 1, 1
	while k<= n:
		total *= term(k)
		k += 1
	return total

def factorial(n):
	"""Return n!"""
	assert n >= 0 and n == int(n), "n must be a nonnegative integer!"
	if n == 0:
		return 1
	else:
		return product(n, lambda k: k)

summation(3, lambda k: k) # 1 + 2 + 3 = 6
summation(3, lambda k: k * k) # 1^2 + 2^2 + 3^2 = 14
summation(3, factorial) # 1! + 2! + 3! = 9
summation(10, lambda k: pow(-1, k) / pow(k, 2)) # -1/1^2 + 1/2^2 - 1/3^2 + 1/4^2 - ... = -pi^2/12  

# Practice: the order-2 composition of a function
def compose(f, x):
	return f(f(x))

def square(x):
	return x * x

def add_2(x):
	return x + 2

# compose(square, 3) # (3 ^ 2) ^ 2 = 81
# compose(add_2, 3) # (3 + 2) + 2 = 7
# compose(exp, 3) # exp(exp(3))

# Practice: the Taylor series for e^x and sin(x)
def taylor_approximate(term, n):
	"""Return a function that is the nth order taylor polynomial.
	term 	-- a function that takes one argument
	n 		-- a nonnegative integer
	"""
	def taylor_approx_at_x(x):	# 这里有curry的思想,把三个参数的函数拆成两个和一个的
		total, k = 0, 0
		while k <= n:
			total += term(x, k)
			k += 1
		return total
	return taylor_approx_at_x

def exp_term(x, k):
	return pow(x, k) / factorial(k)

def sin_term(x, k):
	sign = pow(-1, k % 2 == 1)
	return sign * pow(x, 2*k + 1) / factorial(2*k + 1)

# sin_taylor_approx = taylor_approximate(sin_term, 10)
# sin3 = sin_taylor_approx(3)
# exp_taylor_approx = taylor_approximate(exp_term, 10)
# exp3 = exp_taylor_approx(3)

# 也可以把x直接放到taylor_approximate函数里作为参数，返回该点的估计值，用法如下
# taylor_approximate(exp_term, 3, 10)
# taylor_approximate(sin_term, 3, 10)


