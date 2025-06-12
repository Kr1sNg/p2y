# Write your solution here
# If you use the classes made in the previous exercise, copy them here

class Task:
	id = 0

	@classmethod
	def new_id(cls):
		Task.id += 1
		return Task.id

	def __init__(self, description, programmer, workload):
		self.id = Task.new_id()
		self.description = description
		self.programmer = programmer
		self.workload = workload
		self.mark = False

	def is_finished(self):
		return self.mark
	
	def mark_finished(self):
		self.mark = True
	
	def __str__(self):
		status = "FINISHED" if self.mark else "NOT FINISHED"
		return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

class OrderBook:
	def __init__(self):
		self.__tasks = []
	
	def add_order(self, description, programmer, workload):
		self.__tasks.append(Task(description, programmer, workload))
	
	def all_orders(self):
		return self.__tasks
	
	def programmers(self):
		return list(set([t.programmer for t in self.__tasks]))
	
	def mark_finished(self, id: int):
		for task in self.__tasks:
			if task.id == id:
				task.mark_finished()
				return
		raise ValueError
	
	def unfinished_orders(self):
		return [t for t in self.__tasks if not t.is_finished()]
	
	def finished_orders(self):
		return [t for t in self.__tasks if t.is_finished()]
	
	def status_of_programmer(self, programmer: str):
		if programmer not in self.programmers():
			raise ValueError
		
		fnd_tasks = [t for t in self.__tasks if t.programmer == programmer and t.is_finished()]
		unfnd_tasks = [t for t in self.__tasks if t.programmer == programmer and not t.is_finished()]

		fnd_hrs = sum(t.workload for t in fnd_tasks)
		unfnd_hrs = sum(t.workload for t in unfnd_tasks)

		return (len(fnd_tasks), len(unfnd_tasks), fnd_hrs, unfnd_hrs)

def pic_time(s: str):
	if " " not in str:
		print 

def main():
	command = """
commands:
0 exit
1 add order
2 list finished tasks
3 list unfinished tasks
4 mark task as finished
5 programmers
6 status of programmer"""
	print(command)
	print()
	
	orders = OrderBook()
	while True:
		cmd = int(input("command: "))
		if cmd == 0:
			break
		if cmd == 1:
			desc = str(input("description: "))
			pic_time = (str(input("programmer and workload estimate: ")))
			try:
				pic = pic_time.split(' ')[0]
				time = int(pic_time.split(' ')[1])
				orders.add_order(desc, pic, time)
				print("added!")
				print()
			except:
				print("erroneous input")
				print()
			

		if cmd == 2:
			if len(orders.finished_orders()) == 0:
				print("no finished tasks")
			else:
				for t in orders.finished_orders():
					print(t)
			print()
		
		if cmd == 3:
			unfinished = orders.unfinished_orders()
			if len(unfinished) == 0:
				print("no unfinished tasks")
			else:
				for t in unfinished:
					print(t)
			print()
		
		if cmd == 4:
			try:
				id = int(input("id: "))
				orders.mark_finished(id)
				print("marked as finished")
				print()
			except:
				print("erroneous input")
				print()
			
		
		if cmd == 5:
			for pic in orders.programmers():
				print(pic)
			print()
		
		if cmd == 6:
			pic = input("programmer: ")
			if pic not in orders.programmers():
				print("erroneous input")
				print()
				continue
			tup = orders.status_of_programmer(pic)
			print(f"tasks: finished {tup[0]} not finished {tup[1]}, hours: done {tup[2]} scheduled {tup[3]}")

main()