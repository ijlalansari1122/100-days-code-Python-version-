#  this code will be used for multiple ifs
import calendar


def checkleap(year):

   yearcheck = calendar.isleap(year)
   return yearcheck


Checkyear= int(input('please enter the year'))

if  checkleap(Checkyear) :
    print('correct the year is leapyear')

else:
    print('sorry the year is not leapyear')
