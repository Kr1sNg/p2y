'''
Candies

A gummy candy costs a euros and a chocolate candy costs b euros.
What is the maximum number of candies you can buy if you have c euros?
You may assume that a, b and c are integers in the range 1 ... 100.
In a file candies.py, implement the function count that returns the maximum number of candies.

def count(a, b, c):
    # TODO

if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4

Explanation:
In the first test, a gummy candy costs 3 euros and a chocolate candy costs 4 euros.
You can buy at most 3 candies with 11 euros.
For example, two gummy candies and one chocolate candy cost a total of 10 euros leaving you with 1 euro.
'''

def count(a, b, c):
    na = 0
    nb = 0
    if a < b:
        na += c // a
        nb += (c - (a * na)) // b
    else:
        nb += c // b
        na += (c - (b * nb)) // a
    return na + nb


'''
Result:

def count(a, b, c):
    return c // min(a, b)
    
'''
        

if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4
