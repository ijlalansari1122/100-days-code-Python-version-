

# python function

name1 =input("please enter first  name \n")


name2 =input("please enter second name \n")




def name_adder(n1 ,n2):
    
    add = n1 + " " +n2
    out =  print(f"full name of the student is {add}\n")
    
    return out


name_adder(name1 , name2)