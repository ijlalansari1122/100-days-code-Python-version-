import random

print('WELCOME TO HEADS AND TAILS EXERCISE')

toss = random.randint(0, 1)

if toss == 0:
    print(f'its Tails you have won the toss and its value is {toss}')

elif toss == 1:
    print(f'its Heads  you have won the toss and its value is {toss}')

else:
    print('choose head or tail')
