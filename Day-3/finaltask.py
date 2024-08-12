# Welcome to Treasure Island


print('Welcome to Treasure Island')

print('Your misson is to find the treasure ')


# variables for the game


First_choice =input('Please choose left or right!!!!  ').lower()






# logic for the game

if First_choice == 'left':

       #  second variable for condition
       second_choice =input('What would you do Swim or wait? ').lower()

       if second_choice == 'wait':
          # third variable for the choosing door
          third_choice =input('Which door would you choose ? Red , Blue or Yellow! ' ).lower()

          if third_choice == 'yellow':
             print('Congrats you won!')

          elif third_choice == 'Red' or third_choice == 'Blue':
              print('Game Over')
              exit()
          else:
              print('please choose valid option')
       elif second_choice == 'swim':
           print('Game Over')
           exit()
       else:
           print('Game Over')
           print(exit())

elif First_choice == 'right':
           print('Game Over')
           exit()


else:
    print('Game over !! try again and again')
    print(exit())