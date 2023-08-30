sum_squares = 0
for i in range(1, 101):
  sum_squares += i ** 2

square_sum = sum(range(1, 101)) ** 2

print(square_sum - sum_squares)