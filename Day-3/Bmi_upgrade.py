
#  Bmi calculator

Height = float(input('please enter your height in m:'))

Weight = float(input('please enter your weight in kg:'))


def Bmi_cal(height , weight):
     return round(weight/height**2)


 
Bmi_result =   Bmi_cal(Height, Weight)

print('The Bmi result is ', int(Bmi_result))


 # nested if else for bmi calculation


if Bmi_result <18.5:
    print(f'you are Underweight and bmi is {Bmi_result}')

elif Bmi_result <25:
    print(f'you are normal weight and bmi is {Bmi_result}')

elif Bmi_result < 30:
    print(f'you are over weight and bmi is {Bmi_result}')

elif Bmi_result < 35:
    print(f'you are obese and bmi is {Bmi_result}')
else:print('clinically obese')
            
           
                        
    

 