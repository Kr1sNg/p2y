# str_list = ["123", "-10", "23", "98", "0", "-110"]
# int_list = map(lambda x: int(x), str_list)
# for number in int_list:
# 	print(number)

# def ft_capitalize(my_str: str):
#     first = my_str[0]
#     first = first.upper()
#     return (first + my_str[1:])
# test_list = ["first", "second", "third", "fourth"]
# capitalize = map(ft_capitalize, test_list)
# capi_list = list(capitalize)
# print(capi_list)

# class BankAccount:
#     def __init__(self, account_number: str, name: str, balance: float):
#         self.__account_number = account_number
#         self.name = name
#         self.__balance = balance

#     def deposit(self, amount: float):
#         if amount > 0:
#             self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# a1 = BankAccount("123456", "Randy Riches", 5000)
# a2 = BankAccount("12321", "Paul Pauper", 1)
# a3 = BankAccount("223344", "Mary Millionaire ", 1000000)

# accounts = [a1, a2, a3]

# clients = map(lambda t: t.name, accounts)
# for name in clients:
#     print(name)

# balances = map(lambda t: t.get_balance(), accounts)
# for i in balances:
#     print(i)

class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Write your solution here

# def student_name(course: CourseAttempt):
#     return course.student_name

def names_of_students(attempts: list):
    name_list = list(map(lambda course: course.student_name, attempts))
    return name_list

def course_names(attempts: list):
    courses = list(map(lambda course: course.course_name, attempts))
    return sorted(set(courses))

if __name__== "__main__":
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

    for name in names_of_students([s1, s2, s3]):
        print(name)

    for name in course_names([s1, s2, s3]):
        print(name)
