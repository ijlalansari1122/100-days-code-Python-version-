# fibonacci sequence



fibonacci_sequence = [0, 1]
n = int(input('please specify how many numbers do you want to generate  '))

for i in range(2, n):
    summed = fibonacci_sequence[-1]+ fibonacci_sequence[-2]

    fibonacci_sequence.append(summed)

print('the fibonacci sequence is', fibonacci_sequence)
