# Task 1: Variables and Data Types

# Create three variables: name (string), age (integer), and height (float). Assign values to these variables with your own information.


# Print out a sentence using these variables. For example: "My name is [name], I am [age] years old, and I am [height] feet tall."




name = 'ijlal'

age =23
height =6.2

print(f"My name is {name}, I am {age} years old, and I am {height} feet tall.")

# Task 2: Control Flow
# Write an if-else statement to check if a given number is even or odd. You can take user input for the number.
# Implement a loop to print the square of numbers from 1 to 5.


# if-else statements to check if a given number is even or odd. You can take user input
user_input =int(input('please enter'))

if user_input % 2 == 0:
    print(f'The number {user_input} is even')

elif user_input % 2 == 1:
    print(f'The number {user_input} is odd')

else:print('well the input should be number')



# implementation of a loop to print the square of numbers 1 to 5

data =[1,2,3,4,5]

for i in data:
    squared = pow(i,2)
    print(f'the square of numbers is{squared} ')
#
#
#


#
# Create a function called calculate_square that takes a number as an argument and returns its square.
# Use the function to calculate and print the square of a couple of numbers.


def calculate_square(number):
   return pow(number, 2)

print("Number is " , calculate_square(42))

# Task 4: Lists and Dictionaries
# Create a list named colors with the names of three colors of your choice.
# Add a new color to the list.
colors =['#ffffff', '#dddddd', '#gggg']

colors.append('yellow')

print("the colors in the list are:", colors)



# Create a dictionary named person with keys "name", "age", and "city". Fill in the values with your own information.
# Print out a sentence using the values from the dictionary. For example: "My name is [name], I am [age] years old, and I live in [city]."

dictionary ={'name': 'John', 'age': 23, 'city': 'lahore'}

print(f'my name is :{dictionary['name']} , my age is :{dictionary['age']} and I live in {dictionary['city']}')


