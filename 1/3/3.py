# x = 600851475143 
from math import sqrt

initial_x = 600851475143
x = initial_x

for i in range(2, int(sqrt(initial_x)) + 1):
    while x % i == 0:
        x /= i
        if x == 1:
            print(i)

if x != 1:
    print(int(x))
