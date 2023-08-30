
F = [1, 2]
even = []

for i in range(3, 4*10**6):
    if i == F[-1] + F[-2]:
        F.append(i)

for num in F:
    if num % 2 == 0:
        even.append(num)
        
# print(F)
# print(even)
print(sum(even))