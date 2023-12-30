# Roller coaster  checker

#
# Height =int(input('please enter your  height in cm '))
#
#
# Age =int(input('please enter your  age '))
#
#
# bill = 0
# if Height >=120:
#     if Age <12:
#         bill=5
#         print('child tickets start at $5 ')
#
#     elif Age <=18:
#         bill = 7
#         print('teenage tickets start at $7 ')
#     else:
#         bill = 12
#
#         print('adult tickets start at  $12 ')
#
#     wantsphoto = input('do you want a photo y or n  ')
#     if wantsphoto =='y':
#         bill +=3
#
#     print(f'your final bill is {bill}')
#
# else:print('sorry you cannot ride !!')



# Pizza order



print('Welcome to python pizza delivery')

size =input('what size pizza do you want ? S , M or L  ')

bill =0
if size == 'S':
    bill=15
    print('small pizza start at $15 ')

elif size == 'M':
    bill = 20
    print('medium pizza start at $20 ')


elif size == 'L':
    bill = 25
    print('large pizza start at $25 ')

else: print('please select an option')


# checking if customer require pepparoni

add_pepporoni =input('Do you want pepparoni ? Y or N ')

if add_pepporoni == 'Y' and size == 'S':
   bill +=2
   print('Adding pepporani for small pizza will cost $2 ')



elif add_pepporoni == 'Y' and size == 'M' or  add_pepporoni == 'Y' and size == 'L':
    bill += 3
    print('Adding pepporani for medium and large pizza will cost $3 ')

# checking if customer require extra cheese

extra_cheese =input('Do you want extra cheese ?  y or N ')

if extra_cheese == 'Y':
   bill +=1
   print('Extra cheese will cost $1 ')



print(f'your final bill is {bill}')
