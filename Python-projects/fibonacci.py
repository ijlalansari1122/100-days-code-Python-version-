# fibonacci sequence

print(" <--------Welcome to Fibonacci sequence----> ")


num_limit = int(input("please enter how many fibonacci sequences you want to print:  "))


def fibonacci_sq(num_to_gen):
    fibonacci_sequence = [0, 1]
    for i in range(2, num_to_gen):
        next_num = fibonacci_sequence[-2] + fibonacci_sequence[-1]
        fibonacci_sequence.append(next_num)

    print(f"the fibonacci sequence is {fibonacci_sequence}")


fibonacci_sq(num_limit)
