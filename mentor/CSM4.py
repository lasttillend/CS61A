# Computer Science Mentors 4: OOP and Orders of Growth

# Object Oriented Programming
# 1. (H)OOP
class Baller:
	all_players = []
	def __init__(self, name, has_ball = False):
		self.name = name
		self.has_ball = has_ball
		Baller.all_players.append(self)

	def pass_ball(self, other_player):
		if self.has_ball:
			self.has_ball = False
			other_player.has_ball = True
			return True
		else:
			return False

class BallHog(Baller):
	def pass_ball(self, other_player):
		return False
# 2. 
class TeamBaller(Baller):
	"""An instance of TeamBaller cheers on the team every time
	it passes a ball.
	>>> cheerballer = TeamBaller('Thomas', has_ball=True)
	>>> cheerballer.pass_ball(surya)
	Yay!
	True
	>>> cheerballer.pass_ball(surya)
	I don't have the ball
	False
	"""
	def pass_ball(self, other_player):
		if self.has_ball:
			self.has_ball = False
			other_player.has_ball = True
			print('Yay!')
			return True
		else:
			print("I don't have the ball")
			return False

# 3. OOP version of PingPong
class PingPongTracker:
	"""
	>>> tracker1 = PingPongTracker()
	>>> tracker2 = PingPongTracker()
	>>> tracker1.next()
	1
	>>> tracker1.next()
	2
	>>> tracker2.next()
	1
	"""
	def __init__(self):
		self.current = 0
		self.index = 1
		self.add = True

	def next(self):
		if self.add:
			self.current += 1
		else:
			self.current -= 1
		if has_seven(self.index) or self.index % 7 == 0:
			self.add = not self.add
		self.index += 1
		return self.current

def has_seven(k): # Use this function for your answer below
	if k % 10 == 7:
		return True
	elif k < 10:
		return False
	else:
		return has_seven(k // 10)

# 和使用nonlocal的implement方式比较，一模一样
# def make_pingpong_tracker():
# 	"""Returns a function that returns the next value in the pingpong
# 	sequence each time it is called.
# 	>>> output = []
# 	>>> x = make_pingpong_tracker()
# 	>>> for _ in range(9):
# 	... output += [x()]
# 	>>> output 
# 	[1, 2, 3, 4, 5, 6, 7, 6, 5]
# 	"""
# 	index, current, add = 1, 0, True
# 	def pingpong_tracker():
# 		nonlocal index, current, add
# 		if add:
# 			current += 1
# 		else:
# 			current -= 1
# 		if has_seven(index) or index % 7 == 0:
# 			add = not add
# 		index += 1
# 		return current

# 	return pingpong_tracker

# Orders of Growth
# 1. 
# O(n)
def foo(n):
	for i in range(n):
		print('hello')

# 2. 
# O(2^n)
def strange_add(n):
	if n == 0:
		return 1
	else:
		return strange_add(n - 1) + strange_add(n - 1)
# O(n)
def stranger_add(n):
	if n < 3:
		return n 
	elif n % 3 == 0:
		return stranger_add(n - 1) + stranger_add(n - 2) + stranger_add(n - 3)
	else:
		return n
# O(n^2)
def waffle(n):
	i = 0
	total = 0
	while i < n:
		for j in range(50 * n):
			total += 1
		i += 1
	return total
# O(n^3)
def belgian_waffle(n):
	i = 0
	total = 0
	while i < n:
		for j in range(n ** 2):
			total += 1
		i += 1
	return total
# O(2^n)
def pancake(n):
	if n == 0 or n == 1:
		return n
	# Flip will always perform three operations and return -n.
	return flip(n) + pancake(n - 1) + pancake(n - 2)
# O(n*2^n)
def toast(n):
	i = 0
	j = 0
	stack = 0
	while i < n:
		stack += pancake(n)
		i += 1
	while j < n:
		stack += 1
		j += 1
	return stack
