def get_chainLenght(n):
  final_number = n
  chain = [n]

  while final_number != 1:
    if final_number % 2 == 0:
      final_number = final_number / 2
      chain.append(final_number)
    else: 
      final_number = final_number*3 + 1
      chain.append(final_number)

  return len(chain)

n = 2
max_chain = 0
while max_chain < 1000000:
  if get_chainLenght(n) > max_chain:
    max_chain = get_chainLenght(n)
  n += 1

print(n)
