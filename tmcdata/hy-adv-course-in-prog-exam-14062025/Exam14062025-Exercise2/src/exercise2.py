# Write your solution to exercise 2 here

class Car:
	current_year = 2000

	def __init__(self, brand: str, purchase_year: int, purchase_price: int):
		self.brand = brand
		self.purchase_year = purchase_year
		self.purchase_price = purchase_price
		self.total_distance = 0
		self.total_expense = 0

		if purchase_year > Car.current_year:
			Car.current_year = purchase_year
	
	def set_year(self, new_year: int):
		if new_year > self.purchase_year and new_year > Car.current_year:
			Car.current_year = new_year
		else:
			print("Error: New year must be greater")

	def drive(self, distance_driven: int, cost_per_kilometer: float):
		self.total_distance += distance_driven
		self.total_expense += distance_driven * cost_per_kilometer

	def add_expense(self, expense: int):
		self.total_expense += expense

	def distance_driven_by_car(self):
		return self.total_distance

	def current_value(self):
		return int(self.purchase_price * (0.85 ** (Car.current_year - self.purchase_year)))

	def cost_per_kilometer(self):
		if self.total_distance == 0:
			return 0.0
		depreciation = self.purchase_price - self.current_value()
		total_cost = self.total_expense + depreciation
		return (total_cost / self.total_distance)

	def __str__(self):
		return f"{self.brand}: purchase year {self.purchase_year}, value {self.current_value()} "

if __name__ == "__main__":
	toyota = Car("Toyota", 2020, 10000)
	print(toyota)
	toyota.drive(100, 0.10)
	print(f"Distance driven with Toyota: {toyota.distance_driven_by_car()}")
	toyota.set_year(2021)
	print(f"Value of Toyota in 2021: {toyota.current_value()}")
	print(toyota)
	print(f"Cost per kilometer for Toyota in 2021: {toyota.cost_per_kilometer()}")
	toyota.set_year(2022)
	print(f"Value of Toyota in 2022: {toyota.current_value()}")
	bmw = Car("BMW", 2023, 20000)
	print(f"Value of Toyota after purchasing BMW: {toyota.current_value()}")
	bmw.drive(200, 0.12)
	bmw.drive(300, 0.13)
	print(f"Distance driven with BMW: {bmw.distance_driven_by_car()}")
	print(f"Cost per kilometer for BMW in 2023: {bmw.cost_per_kilometer()}")
	bmw.add_expense(1000)
	print(f"Cost per kilometer for BMW after a 1000 euro service: {bmw.cost_per_kilometer()}")