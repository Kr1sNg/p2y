# Write your solution here:
class Clock:
	def __init__(self, hour: int, minute: int, second: int):
		self.hour = hour
		self.minute = minute
		self.second = second

	def __str__(self):
		return (f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")
	
	def tick(self):
		self.second += 1
		if self.second == 60:
			self.second = 0
			self.minute += 1
			if self.minute == 60:
				self.minute = 0
				self.hour += 1
				if self.hour == 24:
					self.hour = 0
	
	def set(self, hour: int, minute: int):
		self.hour = hour
		self.minute = minute
		self.second = 0

if __name__ == "__main__":
	clock = Clock(23, 59, 55)
	print(clock)
	clock.tick()
	print(clock)
	clock.tick()
	print(clock)
	clock.tick()
	print(clock)
	clock.tick()
	print(clock)
	clock.tick()
	print(clock)
	clock.tick()
	print(clock)

	clock.set(12, 5)
	print(clock)

