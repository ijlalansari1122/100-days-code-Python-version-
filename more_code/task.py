# Number guessing game
import random

attempts =0

randomnum = random.randint(0,10)

while True:
    number_guess = int(input("please enter the number "))
    attempts +=1

    if randomnum == number_guess:
        print(f"Congratulations ! You have generated the number in {attempts} attempts! ")


    elif number_guess > randomnum:
           print("To high!")
    else:
        print("To low!")








































