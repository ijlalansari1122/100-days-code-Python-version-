import random

#Step 1 


word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)



#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

words =['_']*len(chosen_word)


while True:

 guess = input("Hello , can you assign a letter for the hangman game ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

 lives = 5

 if guess == chosen_word:
    
    
    print("Right")
    
    
    
    
 else:
    print("Wrong")
    lives=-1