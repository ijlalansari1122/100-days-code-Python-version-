import random

random_num = random.randint(0, 10)

# nummed = []
x =int(input('plese enter the value  '))
list1 =[]
def values_random():
    # v=random.randint(0,x)
    # nummed.append(random_num)
    while True:
        for i in range(0 ,x):
            v = random.randint(0, 9)
            list1.append(v)
            print(list1)





values_random()

