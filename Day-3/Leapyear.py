# Leap year checker


print("Welcome to leap year checker")


year = int(input('please enter a year '))

if year%4 == 0:

  if year%100 == 0:

    if year%400 ==0:
     print("leap year")
    else:print("not leap year")

  else:print("leap year")

else: print("the year that you entered is not a leap year")