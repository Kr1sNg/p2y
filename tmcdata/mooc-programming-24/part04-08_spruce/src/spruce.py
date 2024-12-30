# Write your solution here
def ft_tree(n):
    i = 1
    while (i <= n):
        print((n - i) * " " + (i * 2 - 1) * "*")
        i += 1
    print((n - 1) * " " + "*")

def spruce(number):
    print("a spruce!")
    ft_tree(number)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)