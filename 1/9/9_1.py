from math import *

def is_square(num):
    root = int(sqrt(num))
    if num / root == root:
        return True
    else:
        return False

multiplication = []
x = 1000
y = x + 1

for i in range(1, y):
    for j in range(1, y):
        if i < j and i**2 + j**2 == (x - i-j)**2:
            if is_square((i**2 + j**2)):
                multiplication.append(i* j* int(sqrt(i**2 + j**2)))
                print(i, j, int(sqrt(i**2 + j**2)), multiplication, end='')
            else:
                exit()

            # n = list(map(is_square, numbers))
            # print(n[i], n[j],  sqrt(32 - n[i] - n[j]))
            # # else:
            # #     exit()

