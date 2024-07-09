import random

# Otp generator 

def otp_gen():
  list1 =[]
  while len(list1)<4:
        
        list1.append(random.randint(0,9))
        
  return list1
  
converted  = int(''.join(map(str, otp_gen())))


print("the otp generated is ", converted)



