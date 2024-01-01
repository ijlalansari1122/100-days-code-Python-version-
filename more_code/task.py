# Number guessing game
import random

attempts = 0

difficulty_level = input('please choose your difficulty level: E = Easy  , N = Normal , M = Medium  and  H = Hard ')

#  Function for difficulty setter

if difficulty_level== 'E' :
        number_ = random.randint(0, 10)
elif difficulty_level ==   'N':
        number_ =  random.randint(0, 500)

elif difficulty_level ==  'M':
        number_=  random.randint(0, 1000)

elif difficulty_level == 'H':
         number_ = random.randint(0, 5000)

else: print("please choose from E , N , M , H" )
 # while loop and if else for number guessing functionility
#
while True:
    number_guess = int(input("please enter the number "))
    attempts +=1

    if  number_guess == number_ :
        print(f"Congratulations ! You have generated the number in {attempts} attempts! ")


    elif  number_guess < number_:
           print("To low try again.")
    else:
        print("To low try again.")








































