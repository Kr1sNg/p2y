'''
You are given three rectangles whose sides are aligned with the horizontal and vertical axes.
Your task is to compute the total area covered by the rectangles.
Overlapping regions are counted only once.
For example, in the following figure the area covered by the rectangles is 16.
The figure corresponds to the example in the code template.

You may assume that all the coordinates are integers in the range -10^9 ... 10^9.
Notice that going through all possible 1x1 rectangles one by one is too slow.
You have to find a more efficient way to calculate the area.
Implement a function area(rec1, rec2, rec3) that returns the total area covered.
The function is given three tuples, each defining one rectangle.
Each tuple contains four integers x_1, y_1, x_2 and y_2:
The top left corner is (x_1,y_1) and the bottom right corner is (x_2,y_2).

def area(rec1, rec2, rec3):
    # TODO

if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16

'''

def square(rec):
    return (abs(rec[0] - rec[2]) * abs(rec[1] - rec[3]))

def area(rec1, rec2, rec3):
    

if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16