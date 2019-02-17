class Worker:
	greeting = 'Sir'
	def __init__(self):
		self.elf = Worker
	def work(self):
		return self.greeting + ', I work'
	def __repr__(self):
		return Bourgeoisie.greeting

class Bourgeoisie(Worker):
	greeting = 'Peon'
	def work(self):
		print(Worker.work(self))
		return 'My job is to gather wealth'

jack = Worker()
john = Bourgeoisie()
jack.greeting = 'Maam'
jack 			# returns Peon No Quotes in interactive session!
				# This is an exception with the _repr_ method- it's meant to display a Python equivalent expression of an object, 
				# so the string it returns won't be with quotes.  All other methods, including __str__, will return strings with quotes.﻿
jack.__repr__() # returns 'Peon' With Quotes!
jack.__str__()	# returns 'Peon' 

### Representation ###
class Bear:
    """A Bear."""
    def __init__(self):
        self.__repr__ = lambda: 'oski'
        self.__str__ = lambda: 'oski the bear'

    def __repr__(self):
        return 'Bear()'

    def __str__(self):
        return 'a bear'

def print_bear():
    oski = Bear()
    print(oski)				# always the same as print(str(oski))
    print(str(oski))		# an instance attribute called __str__ is ignored, only class attributes are found
    print(repr(oski))		# an instance attribute called __repr__ is ignored, only class attributes are found
    print(oski.__repr__()) 	
    print(oski.__str__())	

def repr(x):
    return type(x).__repr__(x)

def str(x):
    t = type(x)
    if hasattr(t, '__str__'):
        return t.__str__(x)
    else:
        return repr(x)
