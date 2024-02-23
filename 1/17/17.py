
one_to_nine = {'one' : 1, 'two' : 2,'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}

tens = {'ten' : 10, 'Eleven' : 11, 'Twelve' : 12, 'Thirteen' : 13, 'Fourteen' : 14,'Fifteen' : 15,'Sixteen' : 16,'Seventeen' : 17,'Eighteen' : 18,'Nineteen' : 19,'Twenty' : 20,'thirty' : 30,'forty' : 40,'fifty' : 50,'sixty' : 60,'seventy' : 70,'eighty' : 80,'ninety' : 90}
exceptions = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90]

numbers = list(range(1, 1001))

#list_of_strings 'one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six humdred', 'seven hundred', 'eight hundred', 'nine hundred, one thousand'
numbers_of_strings = ['onehundred', 'twohundred', 'threehundred', 'fourhundred','fivehundred', 'sixhundred', 'sevenhundred','eighthundred', 'ninehundred', 'onethousand']
# numbers_of_strings = []

# checksecond number since 20 to ...
def check_second_number(sn):
  for key, value in one_to_nine.items():
    if str(sn)[-1] == str(value):
      return key
    
def check_first_number(fn):
  for key, value in tens.items():
    if str(fn)[-2] == str(value)[0]:
      return key
    
#single numbers
for n in numbers:
  lenght = len(str(n))
  if lenght == 1:
    numbers_of_strings.append(check_second_number(n))

#2 digit numbers
  elif lenght == 2:
    if n in exceptions:
      for key, value in tens.items():
        if n == value:
          numbers_of_strings.append(key)
    else:
      first_number = check_first_number(n)
      second_number = check_second_number(n)
      numbers_of_strings.append(f'{first_number}{second_number}')


  if lenght == 3:
    # if there is a single number
    if str(n)[-2] + str(n)[-1] not in str(exceptions):
      if str(n)[-2] == '0':
        for key, value in one_to_nine.items():
          if str(n)[-1] == str(value):
            single = key
            if n == 100*int(str(n)[0]) + int(str(n)[-1]):
              hundred = check_second_number(str(n)[0])
              numbers_of_strings.append(f'{hundred}hundredand{single}')

  #rest of the numbers in tens
      else:
        first_number = check_first_number(str(n)[-2] + str(n)[-1])
        second_number = check_second_number(str(n)[-2] + str(n)[-1])
        normal1 = first_number
        normal2 = second_number
        if n == 100*int(str(n)[0]) + int((str(n)[-2] + str(n)[-1])):
          hundred = check_second_number(str(n)[0])
          numbers_of_strings.append(f'{hundred}hundredand{normal1}{normal2}')

    #if the tens are in exceptions
    if str(n)[-2] + str(n)[-1] in str(exceptions):
      for key, value in tens.items():
        if str(n)[-2] + str(n)[-1] == str(value):
          exception = key
          if n == 100*int(str(n)[0]) + int((str(n)[-2] + str(n)[-1])):
              hundred = check_second_number(str(n)[0])
              numbers_of_strings.append(f'{hundred}hundredand{exception}')

#count letters in each string
def count_number(num):
  n = 0
  for i in range(len(num)):
    n+=1
  return n

#apply function and sum each string
print(numbers)
print(len(numbers_of_strings))
print(numbers_of_strings)
print(sum(map(count_number, numbers_of_strings)))



