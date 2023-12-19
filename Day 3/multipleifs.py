# #  This code will be functions , loops and statements.
# # This code will solve some problem statements
#
# import calendar
#
# # function for checking leap year
# def checkleap(year):
#
#    yearcheck = calendar.isleap(year)
#    return yearcheck
# # using the function to test it
#
#
# Checkyear= int(input('please enter the year'))
# #
# if  checkleap(Checkyear) :
#     print(f'correct the year is leapyear')
# #
# else:
#     print('sorry the year is not leapyear')
# #
#
# # function for band name generator
#
# def Bandnamegen_(first_n , second_n):
#   bandname = first_n + second_n
#   return bandname;
#
#
# # using function for implementing function
#
# F_name = input('please enter the first name ')
# S_name = input('please enter second name generator ')
#
# Bandnamegenerator = Bandnamegen_(F_name , S_name);
#
# if  Bandnamegenerator =='ijlalansari':
#     print('thus the name is being searched')
#
#
# elif Bandnamegenerator == 'prophetmuhammad' or Bandnamegenerator == 'maulaali':
#     print('mashallah')
#
# else: print('please enter a valid name')
#
#
#
#
# sorting bubble
data = [22,1,3,5,6,8,4,3323,232]
#

def random(x ,y):
    x1 = max(x)
    y2 = min(y)
    return x1, y2


fn_called =random(data,data)

print(f'the maximum number is  {fn_called}')
