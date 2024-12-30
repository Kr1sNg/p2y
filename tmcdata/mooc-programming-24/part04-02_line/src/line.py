# Write your solution here

def line(number, text):
    if (text != ""):
        print(text[0] * number)
    elif (text == ""):
        print("*" * number)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "hello")