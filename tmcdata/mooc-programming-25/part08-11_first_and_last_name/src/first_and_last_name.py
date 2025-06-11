# Write your solution here:
class Person:
	def __init__(self, name: str):
		self.name = name
	
	def return_first_name(self):
		parts = (self.name).split(" ")
		first_name = parts[0]
		return first_name
	
	def return_last_name(self):
		parts = (self.name).split(" ")
		last_name = parts[-1]
		return last_name




if __name__ == "__main__":
	peter = Person("Peter Pythons")
	print(peter.return_first_name())

	pin = Person("tom holland")
	print(pin.return_last_name())












