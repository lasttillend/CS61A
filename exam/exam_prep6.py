# Orders of Growth And Linked Lists

### Orders of Growth ###
# 1 
# Orders of growth of running time in terms of n, the number of elements in the input link?
# O(n)
def append(link, value):
	"""Mutates link by adding value to the end of link."""
	if link.rest is Link.empty:
		link.rest = Link(value)
	else:
		append(link.rest, value)
# O(n^2) 
def extend(link1, link2):
	"""Mutates link1 so that all elements of link2 are added
	to the end of link1.
	"""
	while link2 is not Link.empty:
		append(link1, link2.first)
		link2 = link2.rest

# 2
# theta(1)
def g(n):
	if n % 2 == 0 and g(n + 1) == 0:
		return 0
	return 5

# 3
# Orders of growth for a call to explode(n)?
# theta(n)
def boom(n):
	if n == 0:
		return "BOOM!"
	return boom(n - 1)
# theta(n^2)
def explode(n):
	if n == 0:
		return boom(n)
	i = 0
	while i < n:
		boom(n)
		i += 1
	return boom(n)

# 4
# theta(logn)
def dreams(n):
	if n <= 0:
		return n
	if n > 0:
		return n + dreams(n // 2)

# 5
# Give worst-case asymptotic bounds, in terms of m and n, for the running time of the following functions.
# theta(mn)
def a(m, n):
	for i in range(m):
		for j in range(n // 100):
			print('hi')
# theta(m + n)
def b(m, n):
	for i in range(m // 3):
		print('hi')
	for j in range(n * 5):
		print('bye')
# theta(m^2)
def d(m, n):
	for i in range(m):
		j = 0
		while j < i:
			print('hi')
			j = j + 100

# 6
# theta(n^2)
def weighted_random_choice(lst):
	temp = []
	for i in range(len(lst)):
		temp.extend([lst[i]] * (i + 1))
	return random.choice(temp)

# theta(n)
def ice(n):
	skate = n 
	def rink(n):
		nonlocal skate
		print(n)
		if skate > 0:
			skate -= 1
			rink(skate)
		return skate
	return rink(n // 2)

# theta(1)
def olym(pics):
	total, counter = 0, 0
	for i in range(pics):
		while counnter == 0:
			total += (i + counter)
		return total

# theta(n)
def is_palindrome(s):
	if len(s) <= 1:
		return True
	return s[0] == s[-1] and is_palindrome(s[1:-1])

# theta(n)
def is_palindrome2(s):
	for i in range(len(s) // 2):
		if s[i] != s[-i-1]:
			return False
	return True

# theta(3**m*logn)
def camila(m, n):
	if n <= 1:
		return 0
	cabello = 0
	for i in range(3 ** m):
		cabello += i // n 
	return cabello + camila(m - 5, n // 3)

# theta(nlogn)
def ri(na):
	if na < 1:
		return na 
	def han(na):
		i = 1
		while i < na:
			i *= 2
		return i 
	return ri(na / 2) + ri(na / 2) + han(na - 2)

### Linked Lists ###
# 1
def slice_reverse(s, i, j):
	"""
	>>> s = Link(1, Link(2, Link(3)))
	>>> slice_reverse(s, 1, 2)
	>>> s
	Link(1, Link(2, Link(3)))
	>>> s = Link(1, Link(2, Link(3, Link(4, Link(5)))))
	>>> slice_reverse(s, 2, 4)
	>>> s
	Link(1, Link(2, Link(4, Link(3, Link(5)))))
	"""
	start = s  
	for _ in range(i-1):
		start = start.rest
	reverse = Link.empty	# keep track of reversed linked list
	current = start.rest
	for _ in range(j-i):
		temp = current.rest
		current.rest = reverse
		reverse = current
		current = temp
	# start是开始reverse的前一项，且在整个slice过程中一直保持不变
	# start.rest始终指向pos为i的element，即reversed Link的尾部
	# current此时指向pos为j的element
	start.rest.rest = current # 接上尾部
	start.rest = reverse # 接上头部

class Link:
	"""A linked list with a first element and the rest."""
	empty = ()
	def __init__(self, first, rest=empty):
		assert rest is Link.empty or isinstance(rest, Link)
		self.first = first
		self.rest = rest

	@property 	
	def second(self):
		return self.rest.first

	@second.setter
	def second(self, value):
		self.rest.first = value

	def __getitem__(self, i):
		if i == 0:
			return self.first
		else:
			return self.rest[i-1]

	def __len__(self):
		return 1 + len(self.rest)

	def __repr__(self):
		if self.rest:
			rest_str = ', ' + repr(self.rest)
		else:
			rest_str = ''
		return 'Link({0}{1})'.format(self.first, rest_str)
		
	def __str__(self):
		string = '<'
		while self.rest is not Link.empty:
			string += str(self.first) + ' '
			self = self.rest
		return string + str(self.first) + '>'