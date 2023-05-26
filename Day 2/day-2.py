
x = input('Please provide the first num \n')
first_num = int(x)

y = input('Please provide the first num \n')
sec_num = int(y)
choose_Operator = input('please choose the operator  ' + ' +  -  / * \n')

if  choose_Operator == '+' :{
print(f" THe sum is {first_num + sec_num}")
  
}
elif  choose_Operator == '-' :{
print(f"THe subtraction is {first_num - sec_num}")  
    
};
elif  choose_Operator == '/' :{
print(f"The divison is { first_num / sec_num}")  
    
}
elif  choose_Operator == '*' :{
print(f"The multiplication is { first_num * sec_num}") 
    
}      
else :{
print('please choose a valid operation'+"+ - / *")
}  


