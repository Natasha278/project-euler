
def is_palindrome(num):
    num = str(num)
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - 1 - i]:
            return False
    return True
            
palindromes = []

for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i * j):
            palindromes.append(i * j)

print(max(palindromes))

