import random

attempts = 0

difficulty_level = input('Please choose your difficulty level: E = Easy, N = Normal, M = Medium, H = Hard ')

# Function for difficulty setter
if difficulty_level == 'E':
    number_to_guess = random.randint(0, 10)
    print("Difficulty: Easy")
elif difficulty_level == 'N':
    number_to_guess = random.randint(0, 500)
    print("Difficulty: Normal")
elif difficulty_level == 'M':
    number_to_guess = random.randint(0, 1000)
    print("Difficulty: Medium")
elif difficulty_level == 'H':
    number_to_guess = random.randint(0, 5000)
    print("Difficulty: Hard")
else:
    print("Invalid difficulty level. Please choose E, N, M, or H.")
    exit()

# Number guessing loop
while True:
    number_guess = int(input("Please enter your guess: "))
    attempts += 1

    if number_guess == number_to_guess:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif number_guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
