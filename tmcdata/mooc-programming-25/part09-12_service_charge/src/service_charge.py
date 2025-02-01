# WRITE YOUR SOLUTION HERE:
class BankAccount:
	def __init__(self, owner: str, account: str, balance: float):
		if owner != "" and account != "" and balance >= 0:
			self.__owner = owner
			self.__account = account
			self.__balance = balance
		else:
			raise ValueError
	
	def deposit(self, amount: float):
		if amount >= 0:
			self.__balance += amount
			self.__service_charge()
		else:
			raise ValueError
	
	def withdraw(self, amount: float):
		if amount >= 0 and (self.__balance - amount) / 100 <= amount <= self.__balance:
			self.__balance -= amount
			self.__service_charge()
		else:
			raise ValueError
	
	@property
	def balance(self):
		return self.__balance
	
	def __service_charge(self):
		self.__balance -= self.balance / 100
		
if __name__ == "__main__":
	account = BankAccount("Randy Riches", "12345-6789", 1000)
	account.withdraw(100)
	print(account.balance)
	account.deposit(100)
	print(account.balance)



