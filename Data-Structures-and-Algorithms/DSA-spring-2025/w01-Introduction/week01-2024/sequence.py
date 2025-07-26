'''
Each element in a sequence of numbers is the smallest positive integer that does not occur earlier in the sequence and that has the same digit in the beginning and in the end.
The sequence begins as follows:
1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, ...
Your task is to compute the number at the position n in the sequence.
You may assume that n is at most 1000.
In a file sequence.py, implement a function 'generate' that returns the number at the given position.

def generate(n):
    # TODO

if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 2
    print(generate(3)) # 3
    print(generate(10)) # 11
    print(generate(123)) # 1141

'''

def generate(n):
    lst = []
    for i in range(1, 10):
        lst.append(i)
    a = 1000 - 9
    i = 10
    while a > 0:
        i += 1
        if (str(i))[0] == (str(i))[-1]:
            lst.append(i)
            a -= 1
    return lst[n - 1]

'''
# Solution:
def generate(n):
    count = 0
    value = 0
    while count < n:
        value += 1
        if str(value)[0] == str(value)[-1]:
            count += 1
    return value
'''

if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 2
    print(generate(3)) # 3
    print(generate(10)) # 11
    print(generate(123)) # 1141