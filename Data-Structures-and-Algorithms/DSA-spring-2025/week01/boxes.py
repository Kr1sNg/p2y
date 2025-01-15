'''
Boxes

You need to pack products into boxes.
Each box can hold a certain number of products.
How many boxes do you need at least?
For example, if there are 10 products and fits in one box 3 products, you need at least 4 boxes.
For example, you can pack in boxes 3, 3, 2 and 2 products.
Implement boxes.py a function in the file 'min_count' that returns the smallest number of boxes.
The function parameters are:
- product_count: number of products
- box_size: how many products can fit in the box

Your function will be tested using a large number of different tests.
In each test, both parameters are integers between 1 and 100.

def min_count(product_count, box_size):
    # TODO

if __name__ == "__main__":
    print(min_count(10, 3)) # 4
    print(min_count(10, 4)) # 3
    print(min_count(100, 1)) # 100
    print(min_count(100, 100)) # 1
    print(min_count(100, 99)) # 2
    print(min_count(5, 5)) # 1
    print(min_count(5, 6)) # 1
'''


def min_count(product_count, box_size):
    if product_count % box_size == 0:
        return int(product_count / box_size)
    else:
        return 1 + (int(product_count / box_size))


if __name__ == "__main__":
    print(min_count(10, 3)) # 4
    print(min_count(10, 4)) # 3
    print(min_count(100, 1)) # 100
    print(min_count(100, 100)) # 1
    print(min_count(100, 99)) # 2
    print(min_count(5, 5)) # 1
    print(min_count(5, 6)) # 1