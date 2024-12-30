# Copy here code of line function from previous exercise and use it in your solution
def line(number, text):
    if (text != ""):
        print(text[0] * number)
    elif (text == ""):
        print("*" * number)

def shape(n1, c1, n2, c2):
    i = 1
    while (i <= n1):
        line(i, c1)
        i += 1
    i = 0
    while (i < n2):
        line(n1, c2)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")