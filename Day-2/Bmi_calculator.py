


#  Bmi calculator

Height = input('please enter your height in m:')

Weight = input('please enter your weight in kg:')

# Bmi = int(Weight)/float(Height)**2
# print('the bmi is'  , int(Bmi))


def Bmi_cal(height , weight):
    Bmi = int(weight)/float(height)**2
    return Bmi

 
Bmi_result =Bmi_cal(Height, Weight);

print('The Bmi result is ' , int(Bmi_result));



 