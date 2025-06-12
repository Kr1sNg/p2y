# Write your solution here:
class Task:
	task = 1
	def __init__(self, descript: str, pic: str, time: int):
		self.id = Task.task
		Task.task += 1
		self.description = descript
		self.programmer = pic
		self.workload = time
		self.mark = False
	
	def is_finished(self):
		return self.mark
	
	def mark_finished(self):
		self.mark = True
	
	def __str__(self):
		if self.is_finished() == True:
			return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} FINISHED"
		else:
			return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} NOT FINISHED"


class OrderBook:
	def __init__(self):
		self.orders = []
	
	def add_order(self, description: str, programmer: str, workload: int):
		task = Task(description, programmer, workload)
		self.orders.append(task)

	def all_orders(self):
		return self.orders

	def programmers(self):
		pic = []
		# for order in self.orders:
		# 	if order.programmer not in pic:
		# 		pic.append(order.programmer)
		for order in self.orders:
			pic.append(order.programmer)
		return list(set(pic))

	def mark_finished(self, id: int):
		for task in self.orders:
			if task.id == id:
				task.mark_finished()
				return
		raise ValueError
	
	def finished_orders(self):
		finished = []
		for task in self.orders:
			if task.mark == True:
				finished.append(task)
		return finished
	
	def unfinished_orders(self):
		unfinished = []
		for task in self.orders:
			if task.mark == False:
				unfinished.append(task)
		return unfinished
	
	def status_of_programmer(self, programmer: str):
		if programmer not in self.programmers():
			raise ValueError
		fnd = 0
		unf = 0
		fnd_hrs = 0
		unf_hrs = 0
		for task in self.orders:
			if task.programmer == programmer:
				if task.mark == True:
					fnd += 1
					fnd_hrs += task.workload
				else:
					unf += 1
					unf_hrs += task.workload
		return (fnd, unf, fnd_hrs, unf_hrs)




if __name__ == "__main__":
	# t1 = Task("program hello world", "Eric", 3)
	# print(t1.id, t1.description, t1.programmer, t1.workload)
	# print(t1)
	# print(t1.is_finished())
	# t1.mark_finished()
	# print(t1)
	# print(t1.is_finished())
	# t2 = Task("program webstore", "Adele", 10)
	# t3 = Task("program mobile app for workload accounting", "Eric", 25)
	# print(t2)
	# print(t3)

	# orders = OrderBook()
	# orders.add_order("program webstore", "Adele", 10)
	# orders.add_order("program mobile app for workload accounting", "Eric", 25)
	# orders.add_order("program app for practising mathematics", "Adele", 100)

	# for order in orders.all_orders():
	# 	print(order)

	# print()

	# for programmer in orders.programmers():
	# 	print(programmer)

	# orders = OrderBook()
	# orders.add_order("program webstore", "Adele", 10)
	# orders.add_order("program mobile app for workload accounting", "Eric", 25)
	# orders.add_order("program app for practising mathematics", "Adele", 100)

	# orders.mark_finished(1)
	# orders.mark_finished(2)

	# for order in orders.unfinished_orders():
	# 	print(order)

	orders = OrderBook()
	orders.add_order("program webstore", "Adele", 10)
	orders.add_order("program mobile app for workload accounting", "Adele", 25)
	orders.add_order("program app for practising mathematics", "Adele", 100)
	orders.add_order("program the next facebook", "Eric", 1000)

	orders.mark_finished(1)
	orders.mark_finished(2)

	status = orders.status_of_programmer("Adele")
	print(status)