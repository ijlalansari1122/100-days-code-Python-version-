import random


print("Welcome to Number guessing game....  ")
attempts = 0

difficulty_level = input('Please choose your difficulty level: e = easy, n = normal, m = medium, h = hard ')

# Function for difficulty setter
if difficulty_level == 'e':
    number_to_guess = random.randint(0, 10)
    print("Difficulty: easy")
elif difficulty_level == 'n':
    number_to_guess = random.randint(0, 50)
    print("Difficulty: normal")
elif difficulty_level == 'm':
    number_to_guess = random.randint(0, 100)
    print("Difficulty: medium")
elif difficulty_level == 'h':
    number_to_guess = random.randint(0, 500)
    print("Difficulty: hard")
else:
    print("Invalid difficulty level. Please choose your difficulty level: e = easy, n = normal, m = medium, h = hard.")
    

# Number guessing loop
while True:
    number_guess = int(input("Please enter your guess: "))
    attempts =attempts + 1

    if number_guess == number_to_guess:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif number_guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
