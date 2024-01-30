student_height = input('Input a list of student heights ').split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
# print(student_height)



# add =sum(student_height)/len(student_height )


total_height = 0
for height  in student_height:
   total_height +=height

print(total_height)
#
number_of_student = 0
for student  in student_height:
   number_of_student +=1

print(number_of_student)



average_height =round(total_height/number_of_student)

print('the average height is ', average_height)