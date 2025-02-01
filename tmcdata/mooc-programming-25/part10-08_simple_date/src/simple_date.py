# WRITE YOUR SOLUTION HERE:

class SimpleDate:
	def __init__(self, date, month, year):
		self._date = date
		self._month = month
		self._year = year
	
	def __str__(self):
		return (f"{self._date}.{self._month}.{self._year}")
	
	def __gt__(self, other):
		if self._year > other._year:
			return True
		elif self._year < other._year:
			return False
		else:
			if self._month > other._month:
				return True
			elif self._month < other._month:
				return False
			else:
				if self._date > other._date:
					return True
				else:
					return False

	def __lt__(self, other):
		if self._year < other._year:
			return True
		elif self._year > other._year:
			return False
		else:
			if self._month < other._month:
				return True
			elif self._month > other._month:
				return False
			else:
				if self._date < other._date:
					return True
				else:
					return False
	
	def __eq__(self, other):
		return (self._year == other._year and self._month == other._month and self._date == other._date)
	
	def __ne__(self, other):
		return (not (self._year == other._year and self._month == other._month and self._date == other._date))
	
	def __add__(self, add: int):
		yr = add // 360
		mt = (add % 360) // 30
		dy = (add % 360) % 30
		new_day = self._date + dy
		new_mt = self._month + mt
		new_yr = self._year + yr
		if new_day > 30:
			new_day -= 30
			new_mt += 1
		if new_mt > 12:
			new_mt -= 12
			new_yr += 1
		new = SimpleDate(new_day, new_mt, new_yr)
		return new

	def __sub__(self, other):
		return (abs((self._year * 360 + self._month * 30 + self._date) - (other._year * 360 + other._month * 30 + other._date)))


if __name__ == "__main__":
	d1 = SimpleDate(4, 10, 2020)
	d2 = SimpleDate(2, 11, 2020)
	d3 = SimpleDate(28, 12, 1985)

	print(d2-d1)
	print(d1-d2)
	print(d1-d3)
