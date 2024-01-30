student_score = input('Input a list of student scores ').split()

for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

# highest score checker


# highest_score = 0
# for score in student_score:
#     if score>highest_score:
#         highest_score=score
#
# print('the highest score is ', highest_score)



# Lowest score checker


lowest_score = student_score[-2]

for score in student_score:
    if score<lowest_score:
        lowest_score =score



print('the Lowest score is ', lowest_score)

