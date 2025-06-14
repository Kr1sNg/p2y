# from functools import reduce
# my_list = [2, 3, 1, 5]
# sum_of_numbers = reduce(lambda reduced_sum, item: reduced_sum + item, my_list, 0)
# print(sum_of_numbers)


from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_helper(total_cre, attempt):
    return total_cre + attempt.credits

def sum_of_all_credits(attempts: list):
    return reduce(sum_helper, attempts, 0)

def sum_of_passed_credits(attempts: list):
    passed = list(filter(lambda attempt: attempt.grade > 0, attempts))
    return reduce(sum_helper, passed, 0)


def average(attempts: list):
    def helper_sum_grade(total_grade, attempt):
        return total_grade + attempt.grade

    passed = list(filter(lambda attempt: attempt.grade > 0, attempts))
    total_grade = reduce(helper_sum_grade, passed, 0)
    return total_grade / len(passed)

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)