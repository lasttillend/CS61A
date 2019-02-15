class Account:
	"""A bank account that has a non-negative balance."""
	interest = 0.02 			# A class attribute
	def __init__(self, account_holder):
		self.holder = account_holder
		self.balance = 0

	def deposit(self, amount):
		"""Increase the account balance by amount and return the new balance."""
		self.balance = self.balance + amount
		return self.balance

	def withdraw(self, amount):
		"""Decrease the account balance by amount and return the new balance."""
		if amount > self.balance:
			return "Insufficient funds"
		else:
			self.balance = self.balance - amount
			return self.balance

class CheckingAccount(Account):
	"""A bank account that charges for withdraws."""
	withdraw_charge = 1
	interest = 0.01
	def withdraw(self, amount):
		return Account.withdraw(self, amount + self.withdraw_charge)

class SavingsAccount(Account):
	deposit_charge = 2
	def deposit(self, amount):
		return Account.deposit(self, amount - self.deposit_charge)

# Multiple Inheritance
class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
	def __init__(self, account_holder):
		self.holder = account_holder
		self.balance = 1	# a free dollar

