from math import sqrt

def getTriangularNumber(number):
 return sum(range(number + 1))

def getGraterListDivisors():
  n = 1
  numberOfDdivisors = 0

  while numberOfDdivisors < 501:
    triangular_number = getTriangularNumber(n)
    divisors = []

    for i in range(1, int(sqrt(triangular_number) + 1)):
      if triangular_number % i == 0:
        divisors.append(i)
        if i != triangular_number // i:
          divisors.append(triangular_number // i)
    
    numberOfDdivisors = len(divisors)
    n += 1
    
  return triangular_number


print(getGraterListDivisors())


 



