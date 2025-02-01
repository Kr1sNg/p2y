'''
Student Number

The University of Helsinki student number is a series of nine digits.
The first digit is 0 and the last number is a check number that can be used to detect a typing error in the student number.
The check digit is obtained by calculating the sum of the other digits with the factors 3,7,1,3,7,1,3,7 from left to right.
If the sum is a multiple of 10, the check digit is 0.
Otherwise, the check digit is the distance to the next round tens number.
For example, in the student number 012749139, the sum becomes 3 * 0 + 7 * 1 + 1 * 2 + 3 * 7 + 7 * 4 + 1 * 9 + 3 * 1 + 7 * 3 = 91.
The next round tens number is 100, which is the distance to 9.
Therefore, the last digit of the student number is 9.
Implement the function check_number in the file student.py, which indicates whether the sequence of digits given as a parameter is a correctly formed student number.
The function must return True or False.
Your function will be tested on a large number of different number sequences.

def check_number(number):
    # TODO

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False

'''

def check_number(number):
    s = str(number)
    if s[0] != '0':
        return False
    if len(s) != 9:
        return False
    a = (3 * (int(s[0]) + int(s[3]) + int(s[6])) + 7 * (int(s[1]) + int(s[4]) + int(s[7])) + int(s[2]) + int(s[5])) % 10
    print("a: ", a)
    if int(s[8]) != 0:
        if a == 10 - int(s[8]):
            return True
        else:
            return False
    else:
        if a == 0:
            return True
        else:
            return False
    

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False
    print(check_number("059103335"))

'''
Solution:
The following function checks first that the parameter matches the regular expression ^0[0-9]{8}$, i.e., that it is a 0 followed by exactly eight digits.
Then the function computes the check digit and compares it to the last digit.

import re

def check_number(number):
    if not re.match("^0[0-9]{8}$", number):
        return False

    weight = [3, 7, 1, 3, 7, 1, 3, 7]
    result = 0
    for pos in range(8):
        result += weight[pos] * int(number[pos])

    last = (10 - result % 10) % 10
    return int(number[-1]) == last
    
'''
