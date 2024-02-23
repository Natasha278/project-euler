
def getSum(n): 
  n = 2**n
  sum = 0
  for num in str(n):  
    sum += int(num)       
  return sum

print(getSum(1000))