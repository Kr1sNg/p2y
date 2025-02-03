# tee ratkaisusi tänne

class Course:
	def __init__(self, course: str):
		self.__course = course
		self.__grade = 0
		self.__credits = 0
	
	@property
	def course(self):
		return self.__course
	
	@property
	def grade(self):
		return self.__grade
	
	@property
	def credits(self):
		return self.__credits
	
	def add_course(self, grade: int, credits: int):
		if grade < 0 or credits < 0:
			raise ValueError
		if grade >= self.__grade:
			self.__grade = grade
		self.__credits = credits
	
class Function:
	def __init__(self):
		self.__courses = {}
	
	def add_course(self, course: str, grade: int, credits: int):
		if course not in self.__courses:
			self.__courses[course] = Course(course)
		self.__courses[course].add_course(grade, credits)
	
	def get_data(self, course):
		if course in self.__courses:
			return self.__courses[course]
		else:
			return None
	
	def statistics(self):
		if not self.__courses:
			print("No courses available")
			return
		total_courses = 0
		total_grade = 0
		total_cre = 0
		one = ""
		two = ""
		three = ""
		four = ""
		five = ""
		for course in self.__courses.values():
			total_grade += course.grade
			total_cre += course.credits
			total_courses += 1
			if course.grade == 1:
				one += 'x'
			elif course.grade == 2:
				two += 'x'
			elif course.grade == 3:
				three += 'x'
			elif course.grade == 4:
				four += 'x'
			elif course.grade == 5:
				five += 'x'
		mean = total_grade / total_courses
		print(
			f"{total_courses} completed courses, a total of {total_cre} credits\n"
			f"mean {mean:.1f}\n"
			f"grade distribution\n"
			f"5: {five}\n"
			f"4: {four}\n"
			f"3: {three}\n"
			f"2: {two}\n"
			f"1: {one}"
		)

class Application:
	def __init__(self):
		self.__courses = Function()

	def	help(self):
		print("1 add course")
		print("2 get course data")
		print("3 statistics")
		print("0 exit")

	def add_course(self):
		course = input("course: ")
		grade = int(input("grade: "))
		credits = int(input("credit: "))
		self.__courses.add_course(course, grade, credits)
	
	def get_data(self):
		course = input("course: ")
		c = self.__courses.get_data(course)
		if c == None:
			print("no entry for this course")
			return 
		else:
			print(f"{course} ({c.credits} cr) grade {c.grade}")
			return

	def statistics(self):
		self.__courses.statistics()
	
	def	execute(self):
		self.help()
		while True:
			print("")
			command = input("command: ")
			if command == "0":
				break
			elif command == "1":
				self.add_course()
			elif command == "2":
				self.get_data()
			elif command == "3":
				self.statistics()
			else:
				self.help()

application = Application()
application.execute()


