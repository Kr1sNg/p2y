'''
The course material includes two different ways to implement the function count_even:

# implementation 1
def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# implementation 2
def count_even(numbers):
    return sum(x % 2 == 0 for x in numbers)

Compare the efficiencies of the two implementations using a list that contains 10^7 randomly chosen numbers.

'''
import time
import random

# def count_even(numbers):
#     result = 0
#     for x in numbers:
#         if x % 2 == 0:
#             result += 1
#     return result

def count_even(numbers):
    return sum(x % 2 == 0 for x in numbers)

n = 10**7
print("n: ", n)
random.seed(42)
numbers = [random.randint(1, 10**7) for _ in range(n)]

start_time = time.time()
result = count_even(numbers)
end_time = time.time()

print("result: ", result)
print("time: ", round(end_time - start_time, 2), "s")