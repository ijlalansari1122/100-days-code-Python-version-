import calendar

# Nested statements



print("welcome to the roller coaster")

height = int(input("what is your height in cm? "))


if height>=120:
 print("you can ride the roller coaster")
 age =int(input("what is your age?"))
 if age >18:
        print("child$")
 elif age <12:
        print("please pay 12 $")
 elif age >=12 or age >=18:
        print("please pay 7$")
        
else:
    print("sorry this is not allowed")
    









# values swapped

A =int(input('please enter a number'))
B =int(input('please enter a number'))


def valueswapper(a,b):
  c = int()
  a=b
  b=c
  b=a
  del c
  return a,b


print(f'the values swapped funtion has been generated and values are  {valueswapper(A,B)}')




