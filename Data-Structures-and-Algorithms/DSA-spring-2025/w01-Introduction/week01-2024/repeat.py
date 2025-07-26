'''
Repeat

Your task is to find out how long is the shortest string that forms the given string when repeated.
For example, when the input string is abcabcabcabc, the shortest repeating string is abc.
The string consists of the characters a-z and contains at most 100 characters.
In a file repeat.py, implement a function find that returns the length of the shortest repeating string.

def find(s):
    # TODO

if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7

'''


def find(s):
    leng = len(s)
    for i in range(1, leng + 1):
        if (leng % i == 0):
            sub = s[:i]
            if sub * (leng // i) == s:
                return i

# This code will always return the satified i (the worst case i = leng)

    
'''
Result:

def find(s):
    n = len(s)
    for i in range(1, n+1):
        if n%i == 0 and s[:i] * (n//i) == s:
            return i
'''


if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("hoangtathoang")) # 7