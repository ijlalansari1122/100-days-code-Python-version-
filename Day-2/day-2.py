# Tip calculator

print('Welcome to the tip calculator')

Total_bill =int(input('What was the total bill ? '))


num_people =int(input('How many people to split the bill ?'))

perctange_tip =int(input('What percentage tip would you like to give 10,12 or 15?'))


def tipcalculator(T_bill , N_people , per_tip):
    
    return   (T_bill/N_people)+per_tip;






per_pay =tipcalculator(Total_bill,num_people,perctange_tip)


print('Each person should pay' , per_pay,'$')









