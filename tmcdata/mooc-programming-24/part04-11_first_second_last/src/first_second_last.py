# Write your solution here
def first_word(s):
    i = 0
    while (s[i] != " "):
        i += 1
    return (s[0:i])

def second_word(s):
    i = 0
    while (s[i] != " "):
        i += 1
    i += 1
    b = i
    while (i < len(s) and s[i] != " "):
        i += 1
    return (s[b:i])

def last_word(s):
    i = -1
    while (s[i] != " "):
        i -= 1
    i += 1
    return (s[i:])




# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once programmer"
    print(first_word(sentence) + "|")
    print(second_word(sentence))
    print(last_word(sentence))