#lambda_function = lambda x: x * 2
# lambda_function = lambda x, y: x + y
add_number = lambda x, y: x + y
add_number_with_default = lambda x, y=10: x + y
add_number_multiple_2 = lambda x: x * 2
print("Add number", add_number(5, 3))
print("Add number with default parameter", add_number_with_default(5))
print("Add number Multiple 2", add_number_multiple_2(7))

# Function to calculate square of a number
def square(x):
    return x * x
print("Square of 4 is:", square(7))

# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5 is", factorial(5))
print("Factorial of 0 is", factorial(0))

numbers = [1, 2, 3, 4, 5, 6, 7]

# Using map to square each number in the list
squared_numbers = list(map(lambda x: x * x, numbers))
numbers_map = map(lambda x: x * x, numbers)
print("Squared numbers:", squared_numbers)
print("Numbers map:", list(numbers_map))

# Using filter to get even numbers from the list
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)