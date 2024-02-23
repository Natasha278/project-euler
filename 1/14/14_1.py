
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

def get_chainLength(n: int) -> int:
  final_number = n
  chain = [n]

  while final_number != 1:
    if final_number % 2 == 0:
      final_number = final_number / 2
      chain.append(final_number)
    else:
      final_number = final_number * 3 + 1
      chain.append(final_number)

  return len(chain)

n = 2
max_chain = 0
max_number = 0

while n < 1_000_000:
  chain_length = get_chainLength(n)
  if chain_length > max_chain:
    max_chain = chain_length
    max_number = n
  n += 1

print(max_number)  
