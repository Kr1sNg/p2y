# integers = [1, 2, 3, 1, 2, 3, 5, 6, 4, 9, 10, 14, 15]
# even_numbers = filter(lambda number: number % 2 == 0, integers)
# for number in even_numbers:
#     print(number)

# class Fish:
#     """ The class models a fish of a certain spices and weight """
#     def __init__(self, species: str, weight: int):
#         self.species = species
#         self.weight = weight

#     def __repr__(self):
#         return f"{self.species} ({self.weight} g.)"

# if __name__ == "__main__":
#     f1 = Fish("Pike", 1870)
#     f2 = Fish("Perch", 763)
#     f3 = Fish("Pike", 3410)
#     f4 = Fish("Cod", 2449)
#     f5 = Fish("Roach", 210)

#     fishes = [f1, f2, f3, f4, f5]

#     over_a_kilo = filter(lambda fish : fish.weight >= 1000, fishes)

#     for fish in over_a_kilo:
#         print(fish)

class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(attempts: list):
    return (list(filter(lambda t: t.grade >= 1, attempts)))

def attempts_with_grade(attempts: list, grade: int):
    return (list(filter(lambda t: t.grade == grade, attempts)))

def passed_students(attempts: list, course: str):
    passed_course = list(filter(lambda attempt: attempt.course_name == course, attempts))
    passed_name = list(filter(lambda attempt: attempt.grade > 0, passed_course))
    return sorted(list(map(lambda t: t.student_name, passed_name)))

if __name__ == "__main__":
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
    s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

    for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
        print(attempt)
