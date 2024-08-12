import random

print('Welcome to bank roulette program ')

name_list = input('Please provide list of names of paying bill ')
names = name_list.split(',')

# bill_random = random.choice(names)

bill_random = random.randint(0,len(names)-1 )
persontopay=names[bill_random]

print(f'Hurrah {persontopay} you will pay the bill')

