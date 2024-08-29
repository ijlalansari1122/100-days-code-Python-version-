#Step 4

import random
from hangman_words import word_list
from hangman_logo import stages , logo



end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6 


#Testing code
print(logo)
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
           print(f"you have already guessed  {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
      
#TODO-2: - If guess is not a letter in the chosen_word
# #Then reduce 'lives' by 1. 
    if guess not in chosen_word:
              print(f"you have guessed {guess} , which is not in the word")
                  
              lives -=1
              print(stages[lives])

              if lives == 0:
                         
               end_of_game = True            
               print("You lose")  
               break     
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    print(f"{ "".join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

                  