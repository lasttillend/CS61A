# 1 Object Oriented Programming
# 1.1
class Instructor:
	degree = "PhD (Magic)" # this is a class attribute
	def __init__(self, name):
		self.name = name # this is an instance attribute

	def lecture(self, topic):
		print("Today we're learning about " + topic)

dumbledore = Instructor("Dumbledore")
class Student:
	instructor = dumbledore

	def __init__(self, name, ta):
		self.name = name
		self.understanding = 0
		ta.add_student(self)

	def attend_lecture(self, topic):
		Student.instructor.lecture(topic)
		if Student.instructor == dumbledore:
			print(Student.instructor.name + " is awesome!")
		else:
			print("I miss Dumbledore.")
		self.understanding += 1

	def visit_office_hours(self, staff):
		staff.assist(self)
		print("Thanks, " + staff.name)

class TeachingAssistant:
	def __init__(self, name):
		self.name = name
		self.students = {}

	def add_student(self, student):
		self.students[student.name] = student

	def assist(self, student):
		student.understanding += 1

# snape = TeachingAssistant("Snape")
# harry = Student("Harry", snape)
# harry.attend_lecture("potions")

# hermione = Student("Hermione", snape)
# hermione.attend_lecture("herbology")

# hermione.visit_office_hours(TeachingAssistant("Hagrid"))
# print(harry.understanding)
# print(snape.students["Hermione"].understanding)

# Student.instructor = Instructor("Umbridge")
# Student.attend_lecture(harry, "transfiguration") 
# Equivalent to harry.attend_lecture("transfiguration")

# 1.2
class Email:
	"""Every email object has 3 instance attributes: the
	message, the sender name, and the recipient name.
	"""
	def __init__(self, msg, sender_name, recipient_name):
		self.message = msg
		self.sender_name = sender_name
		self.recipient_name = recipient_name

class Mailman:
	"""Each Mailman has an instance attribute clients, which
	is a dictionary that associates client names with client
	objects.
	"""
	def __init__(self):
		self.clients = {}

	def send(self, email):
		"""Take an email and put it in the inbox of the client
		it is addressed to.
		"""
		receiver = self.clients[email.recipient_name]
		receiver.receive(email)

	def register_client(self, client, client_name):
		"""Takes a client object and client_name and adds it to
		the clients instance attributes.
		"""
		self.clients[client_name] = client


class Client:
	"""Every Client has instance attributes name (which is used for
	addressing emails to the clients), mailman (which is used to send
	emails out to other clients), and inbox (a list of all emails the
	client has received.)
	"""
	def __init__(self, mailman, name):
		self.inbox = []
		self.name = name
		self.mailman = mailman

	def compose(self, msg, recipient_name):
		"""Send an email with the given message msg to the given 
		recipent client.
		"""
		email = Email(msg, self.name, recipient_name)
		self.mailman.send(email)

	def receive(self, email):
		"""Take an email and add it to the inbox of this client."""
		self.inbox.append(email)

# 2 Inheritance
class Pet(object):
	def __init__(self, name, owner):
		self.is_alive = True
		self.name = name
		self.owner = owner

	def eat(self, thing):
		print(self.name + " ate a " + str(thing) + "!")

	def talk(self):
		print(self.name)

class Dog(Pet):
	def __init__(self, name, owner):
		Pet.__init__(self, name ,owner)

	def talk(self):
		print(self.name + ' says woof!')

class Cat(Pet):
	def __init__(self, name, owner, lives=9):
		Pet.__init__(self, name, owner)
		self.lives = lives

	def talk(self):
		"""A cat says meow! when asked to talk."""
		print(self.name + ' says meow!')

	def lose_life(self):
		"""A cat can only lose a life if they have at least one life.
		When lives reaches zero, 'is_alive' becomes False.
		"""
		if self.lives >= 1:
			self.lives -= 1
		if self.lives == 0:
			self.is_alive = False

class NoisyCat(Cat):
	"""A Cat that repeats things twice."""
	def talk(self):
		"""Repeat what a Cat says twice."""
		for _ in range(2):
			Cat.talk(self)

# 2.4
class Yolo:
	def __init__(self, motto):
		self.motto = motto

	def g(self, num):
		return num + self.motto