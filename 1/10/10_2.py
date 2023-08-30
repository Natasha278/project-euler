from math import sqrt

def factor(num):
  factors = []
  for i in range(2, int(sqrt(num)) + 1):
    while num % i == 0:
      num /= i

  if num != 1:
    factors.append(num)

  return factors

def is_prime(num):
  if num in factor(num):
    return True
  else:
    return False
 
x = 2000000
squares = [x]

while x > 0:
    x = int(sqrt(x))
    squares.append(x)
    if x == int(sqrt(x)):
      break

primes = []

for i in range(len(squares) - 1):
  for j in range(squares[i], squares[i+1], -1):
    if is_prime(j):
      primes.append(j)
print(sum(primes))