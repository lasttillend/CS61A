# 1.7.1 sum of the digits of positive interger n
def sum_digits(n):
	"""Return the sum of the digits of positive integer n."""
	if n < 10:
		return n
	else:
		all_but_last, last = n // 10, n % 10
		return sum_digits(all_but_last) + last

# 1.7.2 Mutual Recursion
def is_even(n):
	if n == 0:
		return True
	else:
		return is_odd(n-1)

def is_odd(n):
	if n == 0:
		return False
	else:
		return is_even(n-1)

def is_even(n):
	if n == 0:
		return True
	else:
		if (n-1) == 0:
			return False
		else:
			return is_even((n-1)-1)

result = is_even(4)

# Luhn algorithm: mutual recursion
def split(n):
	return n // 10, n % 10

def luhn_sum(n):
    """Return the digit sum of n computed by the Luhn algorithm.

    >>> luhn_sum(2)
    2
    >>> luhn_sum(12)
    4
    >>> luhn_sum(42)
    10
    >>> luhn_sum(138743)
    30
    >>> luhn_sum(5105105105105100) # example Mastercard
    20
    >>> luhn_sum(4012888888881881) # example Visa
    90
    >>> luhn_sum(79927398713) # from Wikipedia
    70
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    """Return the Luhn sum of n, doubling the last digit."""
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

# 1.7.3 Printing in Recursive Functions
def cascade(n):
	"""Print a cascade of prefixes of n."""
	if n < 10:
		print(n)
	else:
		print(n)
		cascade(n // 10)
		print(n)

def inverse_cascade(n):
	grow(n)
	print(n)
	shrink(n)

def f_then_g(f, g, n):
	if n:
		f(n)
		g(n)
grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)
inverse_cascade(1234)

# More mutual recusion examples
# 1. Hofstader Sequence
"""
Hofstadter Female and Male sequences are defined by:
    F(0) = 1
    M(0) = 0
    F(n) = n - M(F(n - 1)), n > 0
    M(n) = n - F(M(n - 1)), n > 0
"""
def hofstader_female(n):
    if n < 0:
        return
    elif n == 0:
        return 1
    else:
        return n - hofstader_male(hofstader_female(n - 1))

def hofstader_male(n):
    if n < 0:
        return
    elif n == 0:
        return 0
    else:
        return n - hofstader_female(hofstader_male(n - 1))

print("F:", end = " ")
for i in range(20):
    print(hofstader_female(i), end = " ")

print("\n")
print("M:", end = " ")
for i in range(20):
    print(hofstader_male(i), end = " ")

