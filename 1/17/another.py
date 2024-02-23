one_to_nine = {'one' : 1, 'two' : 2,'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}

n = list(range(21, 26))

sn = 28

for key, value in one_to_nine.items():
  if str(sn)[1] == str(value):
    print(key)


# def check_second_number(sn):
#   for key, value in one_to_nine.items():
#     if sn[1] == value:
#       return key
    
# print(check_second_number(n))    