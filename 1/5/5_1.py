import math

for i in range(1, 10**99):
    for j in range(2, 21):
        if i % j != 0:
            break
        if j == 20:
            print(i)
            exit()
