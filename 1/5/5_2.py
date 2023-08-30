from math import prod, sqrt

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

# print(factor(239847234))

max_freq = {}
for i in range(2, 21):
  factors = factor(i)
  for (key, value) in factors.items():
    if key not in max_freq:
      max_freq[key] = 1
    else:
      max_freq[key] = max(max_freq[key], value)


ans = 1
for (key, value) in max_freq.items():
  ans *= key ** value

print(ans)