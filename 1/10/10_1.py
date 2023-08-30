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
  
primes = []
for i in range(2, 2*(10**6) +1):
  if is_prime(i):
    primes.append(i)
print(sum(primes))