# Q1
# O(2^n)
def carpe_noctem(n):
	if n <= 1:	# this block is O(1) on its own
		return n 
	return carpe_noctem(n - 1) + carpe_noctem(n - 2) # two recursive calls
# O(n^2*2^n)
def yolo(n):
	if n <= 1: # this block is O(1) on its own
		return 5
	sum = 0	# O(1)
	for i in range(n): # this block is O(n) times...
		sum += carpe_noctem(n) # whatever the OOG of carpe_noctem is.(In fact, O(2^n))
	return sum + yolo(n - 1) # and then there's another recursive call


# Exercise 1
# O(logn)
def mystery1(n):
	n, result = str(n), '' # str(n) is O(logn)
	num_digits = len(n) # len(n) is O(1)
	for i in range(num_digits):
		result += n[num_digits - i - 1]
	return result

# O(1)	Note: The input n doesn't even matter!
def mystery2(n):
	n, result = 5, 0
	while n <= 3000:
		result += mystery1(n // 2)
		n += 1
	return result

# Exercise 2
# O(logn)
def mystery3(n):
	if n < 0 or n <= sqrt(n):
		return n 
	return n + mystery3(n // 3)
# O(logn)
def mystery4(n):
	if n < 0 or sqrt(n) <= 50:
		return 1
	return n * mystery4(n // 2)
# O(sqrt(n))
def mystery5(n):
	for _ in range(int(sqrt(n))):
		n = 1 + 1
	return n

# Exercise 3
# O(nlogn)
def mystery6(n):
	while n > 1:
		x = n 
		while x > 1:
			print(n, x)
			x = x // 2
		n -= 1
# O(n)
def mystery7(n):
	result = 0
	for i in range(n // 10):
		result += 1
		for j in range(10):
			result += 1
			for k in range(10 // n):
				result += 1
	return result

# Exercise 4
# O(n^2logn)
def mystery8(n):
	if n == 0: return ''
	result, stringified = '', str(n)
	for digit in stringified:
		for _ in range(n):
			result += digit
	result += mystery8(n - 1)
	return result
# O(n^2) 答案说是O(n)，感觉不对
def mystery9(n):
	total = 0
	for i in range(1, n):
		total *= 2
		if i % n == 0: # this if-statement never happens
			total *= mystery9(n - 1)
			total *= mystery9(n - 2)
		elif i == n // 2: # this only happens once
			for j in range(1, n):
				total *= j
	return total

# Exercise 5
# O(n)
def mystery10(n):
	if n > 0:
		r1 = mystery10(-n)
		r2 = mystery10(n - 1)
		return r1 + r2
	return 1
# O(nlogn)	We make O(2^logn) = O(n) recursive calls, and each recursive call does logn work.
def mystery11(n):
	if n < 1: return n 
	def mystery12(n):
		i = 1
		while i < n:
			i *= 2
		return i
	return mystery11(n / 2) + mystery11(n / 2) + mystery12(n - 2)

# Exercise 6
# The orders of growth should now be functions of m and n.
# O(3^m*logn)
def mystery13(m, n):
	if n <= 1:
		return 0
	result = 0
	for i in range(3 ** m):
		result += i // n 
	return result + mystery13(m - 5, n // 3)
# O(m+n*sqrt(n))
def mystery14(m, n):
	result = 0
	for i in range(1, m):
		j = i * i 
		while j <= n:
			result, j = result + j, j + 1
	return result

# Exercise 7
# Define n to be the length of the input list. How much memory does the
# following program use as a function of n?
# O(n^2)
import random
def weighted_random_choice(lst):
	temp = []
	for i in range(len(lst)):
		temp.extend([lst[i] * (i + 1)])
	print("temp is ", temp)
	return random.choice(temp)

# Exercise 8
# O(logn)
def index_exists(A):
	def helper(lower, upper):
		if lower >= upper:
			return A[upper] == upper
		mid_idx = (lower + upper) // 2
		if A[mid_idx] == mid_idx:
			return True
		elif A[mid_idx] > mid_idx:
			return helper(lower, mid_idx - 1)
		else:
			return helper(mid_idx + 1, upper)

	return helper(0, len(A) - 1)