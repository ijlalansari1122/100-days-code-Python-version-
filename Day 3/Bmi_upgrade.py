
#  Bmi calculator

Height = float(input('please enter your height in m:'))

Weight = float(input('please enter your weight in kg:'))


def Bmi_cal(height , weight):
    Bmi = round(weight/height**2)
    return Bmi

 
Bmi_result =Bmi_cal(Height, Weight);
print('The Bmi result is ' , int(Bmi_result));

if Bmi_result <18.5:
        print(f"underweight");
elif Bmi_result < 25:
        print("Normal weight")
elif Bmi_result < 30:
        print("overweight")
elif Bmi_result < 35:
        print("obese")
else:
    print("clinically obese")
    
            
           
                        
    

 