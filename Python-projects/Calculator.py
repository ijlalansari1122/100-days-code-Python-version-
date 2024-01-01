# This code will be used for making a calculator
import math

num1 =int(input("please enter first number "))

num2 =int(input("please enter second number "))

op =input("please choose operator + - / *  ")


def calculator(x):
 match x:
    case '+':
       sum = num1 +num2
       print(f'the sum of the numbers is {sum} ')

    case '-':
        sub = num1 - num2
        print(f'the subtracted value of the numbers is {sub} ')
    case '*':
        product = num1 * num2
        print(f'the product of the numbers is {product} ')
    case '/':
         if num2 != 0:
          divided = num1 / num2
          print(f'the divided value of the numbers is {divided} ')
         else:print('the divison by zero is not allowed ')

 calculator(op)
