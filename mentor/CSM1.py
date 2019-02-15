# Computer Science Mentors 1

# Recursion
"""
1. 	Write a function is_sorted that takes in an integer n and returns 
	true if the digits of that number are increasing from right to left.
"""
def is_sorted(n):
	"""
	>>> is_sorted(2)
	True
	>>> is_sorted(22222)
	True
	>>> is_sorted(9876543210)
	True
	>>> is_sorted(9087654321)
	False
	"""
	assert n >= 0 and n == int(n), "n must be a nonnegative integer"
	if n < 10:
		return True
	else:
		return (n // 10 % 10 >= n % 10) and is_sorted(n // 10)

# Tree Recursion
"""
1. 	Mario needs to jump over a series of Piranha plants, represented as a string of 0’s
	and 1’s. Mario only moves forward and can either step (move forward one space) or
	jump (move forward two spaces) from each position. How many different ways can
	Mario traverse a level without stepping or jumping into a Piranha plant? Assume
	that every level begins with a 1 (where Mario starts) and ends with a 1 (where Mario
	must end up).
"""
def mario_number(level):
	"""
	Return the number of ways that Mario can traverse the
	level, where Mario can either hop by one digit or two
	digits each turn. A level is defined as being an integer
	with digits where a 1 is something Mario can step on and 0
	is something Mario cannot step on.
	>>> mario_number(10101)
	1
	>>> mario_number(11101)
	2
	>>> mario_number(100101)
	0
	"""
	if level == 1:
		return 1
	elif level % 10 == 0:	# 末位是0最后一定跳不到1上
		return 0
	else:
		return mario_number(level // 10) + mario_number(level // 100)

# level也可以是字符串
def mario_number2(level):
    """Return the number of ways that Mario can perform a sequence of steps or jumps to reach the end of the level without ever landing in a Piranha plant. Assume that every level begins and ends with a dash.
    >>> mario_number2('-P-P-')   # jump, jump
    1
    >>> mario_number2('-P-P--')   # jump, jump, step
    1
    >>> mario_number2('--P-P-')  # step, jump, jump
    1
    >>> mario_number2('---P-P-') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number2('-P-PP-')  # Mario cannot jump two plants
    0
    >>> mario_number2('----')    # step, jump ; jump, step ; step, step, step
    3
    >>> mario_number2('----P----')
    9
    >>> mario_number2('---P----P-P---P--P-P----P-----P-')
    180
    """
    if len(level) == 0 or level[0] == 'P':
        return 0
    elif len(level) <= 2:
        return 1
    else:
        return mario_number2(level[1:]) + mario_number2(level[2:])

"""
2. 	Implement the function make_change. You may not need to use all the lines.
"""
def make_change(n):
	"""Write a function, make_change that takes in an
	integer amount, n, and returns the minimum number
	of coins we can use to make change for that n,
	using 1-cent, 3-cent, and 4-cent coins.
	Look at the doctests for more examples.
	>>> make_change(5)
	2
	>>> make_change(6) # tricky! Not 4 + 1 + 1 but 3 + 3
	2
	"""
	if n < 1:
		return 0
	elif n == 1 or n == 3 or n == 4:
		return 1
	elif n == 2:
		return 2
	else:
		return min(1 + make_change(n-4), 2 + make_change(n-2*3)) # 尽可能用1枚4或者2枚3

# Date Abstraction
"""
1. 	The following is an Abstract Data Type (ADT) for elephants. Each elephant keeps
	track of its name, age, and whether or not it can fly. Given our provided constructor,
	fill out the selectors:
"""
def elephant(name, age, can_fly):
	"""
	Takes in a string name, an int age, and a boolean can_fly.
	Constructs an elephant with these attributes.
	>>> dumbo = elephant("Dumbo", 10, True)
	>>> elephant_name(dumbo)
	'Dumbo'
	>>> elephant_age(dumbo)
	10
	>>> elephant_can_fly(dumbo)
	True
	"""
	return [name, age, can_fly]
def elephant_name(e):
	return e[0]
def elephant_age(e):
	return e[1]
def elephant_can_fly(e):
	return e[2]

"""
2. 	This function returns the correct result, but there’s something 
	wrong about its implementation. How do we fix it?

	def elephant_roster(elephants):
		return [elephant[0] for elephant in elephants]
"""
def elephant_roster(elephants):
	"""
	Takes in a list of elephants and returns a list of their
	names.
	"""
	return [elephant_name(e) for e in elephants] # DO NOT break the abstraction barrier!

"""
3. 	Fill out the following constructor for the given selectors.
"""
def elephant(name, age, can_fly):
	return [[name, age], can_fly]

def elephant_name(e):
	return e[0][0]
def elephant_age(e):
	return e[0][1]
def elephant_can_fly(e):
	return e[1]

"""
4. 	How can we write the fixed elephant_roster function for the constructors and
	selectors in the previous question?
	Ans: We don't need to change it because we treat elephant as an abstract data 
	type and use selectors to access its name.
"""

"""
5. 	(Optional) Fill out the following constructor for the given selectors
"""
def elephant(name, age, can_fly):
	"""
	>>> chris = elephant("Chris Martin", 38, False)
	>>> elephant_name(chris)
	'Chris Martin'
	>>> elephant_age(chris)
	38
	>>> elephant_can_fly(chris)
	False
	"""
	def select(command):
		elephant_dict = {"name": name, "age": age, "can_fly": can_fly}
		return elephant_dict[command]

	return select

	 # def select(command):
  #       if command == "name": return name
  #       elif command == "age": return age
  #       elif command == "can_fly": return can_fly
  #       else: return "something wrong!"
  #   return select

def elephant_name(e):
	return e("name")

def elephant_age(e):
	return e("age")

def elephant_can_fly(e):
	return e("can_fly")











