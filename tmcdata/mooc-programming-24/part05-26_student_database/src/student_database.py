# Write your solution here
def add_student(students: dict, name: str):
	if name not in students:
		students[name] = {}

def print_student(students: dict, name: str):
	if not name in students:
		print(f"{name}: no such person in the database")
		return
	students_completed_courses = students[name]
	print(f"{name}:")
	if len(students_completed_courses) == 0:
		print("no completed courses")
	else:
		print(f" {len(students_completed_courses)} completed courses:")
		sum_grade = 0
		leng = len(students_completed_courses)
		for course, grade in students_completed_courses.items():
			course_grade = grade[1]
			print(f"  {course} {course_grade}")
			sum_grade += course_grade
		print(f" average grade {sum_grade / leng}")

		
# [][name: {(str, int), (str, int)}]

def add_course(students: dict, name: str, completion: tuple):
    students_completed_courses = students[name]
    course_name = completion[0]
    course_grade = completion[1]
    # failed course is not recorded in the database
    if course_grade==0:
        return
    # if previous grade is higher, new grade is not recorded in the database
    if course_name in students_completed_courses:
        if students_completed_courses[course_name][1] > course_grade:
            return
    students_completed_courses[course_name] = completion

def summary(students: dict):
	print(f"students {len(students)}")
	most_courses_count = 0
	best_avg_grade = 0
	for name, completions in students.items():
		if len(completions) > most_courses_count:
			most_courses = name
			most_courses_count = len(students[most_courses])
		sum = 0
		for course, grade in completions.items():
			sum += grade[1]
		if len(completions) == 0:
			avg = 0
		else:
			avg = sum / len(completions)
		if avg > best_avg_grade:
			best_avg_grade = avg
			best = name
	print(f"most courses completed {most_courses_count} {most_courses}")
	print(f"best average grade {best_avg_grade} {best}")

if __name__ == "__main__":
	students = {}
	add_student(students, "Emily")
	add_student(students, "Peter")
	add_course(students, "Emily", ("Software Development Methods", 4))
	add_course(students, "Emily", ("Software Development Methods", 5))
	add_course(students, "Peter", ("Data Structures and Algorithms", 3))
	add_course(students, "Peter", ("Models of Computation", 0))
	add_course(students, "Peter", ("Data Structures and Algorithms", 2))
	add_course(students, "Peter", ("Introduction to Computer Science", 1))
	add_course(students, "Peter", ("Software Engineering", 3))
	summary(students)
	summary(students)
