'''
Year 2025

Year 2025 is a special year because (20+25)^2=2025 that is, the year number is equal to the square of the sum of its left and right halves.
Implement in the file special.pya function check_year that reports whether the year given as a parameter is a specific year.
The function should return True or False.
Your function is tested using a large number of different tests.
Each test uses a year number between 1000 and 9999.

def check_year(year):
    # TODO

if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False

'''

def check_year(year):
    left = int((str(year))[:2])
    right = int((str(year))[2:])
    return ((left + right)**2 == year)


if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False
