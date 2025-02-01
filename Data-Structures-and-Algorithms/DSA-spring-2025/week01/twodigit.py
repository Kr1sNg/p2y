'''
Your task is to count how many numbers in the range [a,b] consist of the digits 2 and 5 only. For example, in the range [1,100] the numbers are 2, 5, 22, 25, 52 and 55, and thus the answer is 6.
In a file twodigit.py, implement the function count_numbers that counts the desired numbers in the range. The function is given the parameters a and b representing the end points of the range.
Your function will be tested using many different ranges. In each test, 1 \le a \le b \le 10^9.
You must implement the function efficiently so that the solution is returned quickly even for long ranges.
def count_numbers(a, b):
    # TODO

if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512

'''

# def count_numbers(a, b):
#     count = 0
#     i = a
#     while i <= b:
#         s = str(i)
#         j = 0
#         while j < len(s):
#             if s[j] in "25":
#                 if j + 1 == len(s):
#                     count += 1
#                 j += 1
#             else:
#                 break
#         i += 1
#     return count

def count_numbers(a, b):
    count = 0
    digit = ['2', '5']
    
    while digit:
        num = digit.pop()
        num_int = int(num) 
        if num_int > b:
            continue
        if num_int >= a:
            count += 1
        digit.append(num + '2')
        digit.append(num + '5')
	
    return count
            

if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512

'''
# SOLUTION:
def count_numbers(a, b):
    numbers = [2, 5]
    count = 0

    for number in numbers:
        if a <= number <= b:
            count += 1

        if number > b: break

        numbers.append(number * 10 + 2)
        numbers.append(number * 10 + 5)

    return count
'''