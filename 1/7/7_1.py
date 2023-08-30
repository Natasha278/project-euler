from math import sqrt

def factor(num):
  factors = dict()
  for i in range(2, int(sqrt(num)) + 1):
    while num % i == 0:
      num /= i

      if i not in factors.keys():
        factors[i] = 1
      else:
        factors[i] += 1

  if num != 1:
    factors[num] = 1

  return factors