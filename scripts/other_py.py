from functools import reduce
from collections import Counter

numbers = [1, 2, 3, 4, 5, 6, 7]

# Using reduce to calculate the sum of all numbers in the list
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_of_numbers)

# Using reduce to calculate the product of all numbers in the list
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product_of_numbers)

# Using reduce to find the maximum number in the list
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum number:", max_number)

# Using reduce to find the minimum number in the list
min_number = reduce(lambda x, y: x if x < y else y, numbers)
print("Minimum number:", min_number)

# Using reduce to concatenate strings in a list
strings = ["Hello", " ", "World", "!"]
concatenated_string = reduce(lambda x, y: x + y, strings)
print("Concatenated string:", concatenated_string)

# Using reduce to find the length of the longest string in a list
def longest_string_length(strings):
    return reduce(lambda x, y: len(x) if len(x) > len(y) else len(y), strings)
print("Length of the longest string:", longest_string_length(strings))

# Using reduce to find the sum of squares of numbers in a list
def sum_of_squares(numbers):
    return reduce(lambda x, y: x + y * y, numbers, 0)
print("Sum of squares:", sum_of_squares(numbers))

# Using reduce to flatten a list of lists
def flatten_list_of_lists(lists):
    return reduce(lambda x, y: x + y, lists)
print("Flattened list:", flatten_list_of_lists([[1, 2], [3, 4], [5]]))

# Using reduce to find the greatest common divisor (GCD) of a list of numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def gcd_of_list(numbers):
    return reduce(gcd, numbers) 
print("GCD of the list:", gcd_of_list([48, 64, 16, 32]))

# Using reduce to find the least common multiple (LCM) of a list of numbers
def lcm(a, b):
    return a * b // gcd(a, b)
def lcm_of_list(numbers):
    return reduce(lcm, numbers)
print("LCM of the list:", lcm_of_list([4, 6, 8]))

# Using reduce to count the occurrences of each character in a string
def char_count(string):
    return reduce(lambda count, char: count.update({char: count.get(char, 0) + 1}) or count, string, {})
print("Character count:", char_count("hello world"))

# Using reduce to find the longest word in a list of words
def longest_word(words):
    return reduce(lambda x, y: x if len(x) > len(y) else y, words)
print("Longest word:", longest_word(["apple", "banana", "cherry", "date"]))

# Using reduce to find the average of a list of numbers
def average(numbers):
    total = reduce(lambda x, y: x + y, numbers)
    return total / len(numbers) if numbers else 0
print("Average of the list:", average(numbers))

# Using reduce to find the median of a list of numbers
def median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]
print("Median of the list:", median(numbers))

# Using reduce to find the mode of a list of numbers
from collections import Counter
def mode(numbers):
    if not numbers:
        return None
    count = Counter(numbers)
    max_count = max(count.values())
    modes = [num for num, cnt in count.items() if cnt == max_count]
    return modes if len(modes) > 1 else modes[0]
print("Mode of the list:", mode(numbers))

# Using reduce to find the range of a list of numbers
def range_of_list(numbers):
    if not numbers:
        return 0
    return max(numbers) - min(numbers)
print("Range of the list:", range_of_list(numbers))

# Using reduce to find the sum of digits in a number
def sum_of_digits(number):
    return reduce(lambda x, y: x + int(y), str(number), 0)
print("Sum of digits in 12345:", sum_of_digits(12345))

# Using reduce to find the product of digits in a number
def product_of_digits(number):
    return reduce(lambda x, y: x * int(y), str(number), 1)
print("Product of digits in 12345:", product_of_digits(12345))

# Using reduce to reverse a string
def reverse_string(string):
    return reduce(lambda x, y: y + x, string, "")
print("Reversed string of 'hello':", reverse_string("hello"))

# Using reduce to find the first non-repeating character in a string        
def first_non_repeating_char(string):
    count = Counter(string)
    return reduce(lambda x, y: y if count[y] == 1 else x, string, None)
print("First non-repeating character in 'swiss':", first_non_repeating_char("swiss"))

# Using reduce to find the longest palindrome in a list of strings
def longest_palindrome(words):
    def is_palindrome(word):
        return word == word[::-1]
    return reduce(lambda x, y: y if is_palindrome(y) and len(y) > len(x) else x, words, "")
print("Longest palindrome in the list:", longest_palindrome(["racecar", "level", "deified", "hello", "world"]))

# Using reduce to find the sum of squares of even numbers in a list
def sum_of_squares_of_evens(numbers):
    return reduce(lambda x, y: x + y * y if y % 2 == 0 else x, numbers, 0)
print("Sum of squares of even numbers:", sum_of_squares_of_evens(numbers))

# Using reduce to find the sum of cubes of odd numbers in a list
def sum_of_cubes_of_odds(numbers):
    return reduce(lambda x, y: x + y ** 3 if y % 2 != 0 else x, numbers, 0)
print("Sum of cubes of odd numbers:", sum_of_cubes_of_odds(numbers))

# Using reduce to find the sum of squares of prime numbers in a list
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True 
print("Is 7 prime?", is_prime(7))

def sum_of_squares_of_primes(numbers):
    return reduce(lambda x, y: x + y * y if is_prime(y) else x, numbers, 0)
print("Sum of squares of prime numbers:", sum_of_squares_of_primes(numbers))

# Using reduce to find the sum of cubes of composite numbers in a list
def is_composite(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False
print("Is 4 composite?", is_composite(4))

# Using reduce to find the sum of cubes of composite numbers in a list
def sum_of_cubes_of_composites(numbers):
    return reduce(lambda x, y: x + y ** 3 if is_composite(y) else x, numbers, 0)
print("Sum of cubes of composite numbers:", sum_of_cubes_of_composites(numbers))

# Using reduce to find the sum of squares of Fibonacci numbers in a list
def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n
def sum_of_squares_of_fibonacci(numbers):
    return reduce(lambda x, y: x + y * y if is_fibonacci(y) else x, numbers, 0)
print("Sum of squares of Fibonacci numbers:", sum_of_squares_of_fibonacci(numbers))

# Using reduce to find the sum of cubes of Lucas numbers in a list
def is_lucas(n):
    a, b = 2, 1
    while a < n:
        a, b = b, a + b
    return a == n
def sum_of_cubes_of_lucas(numbers):
    return reduce(lambda x, y: x + y ** 3 if is_lucas(y) else x, numbers, 0)
print("Sum of cubes of Lucas numbers:", sum_of_cubes_of_lucas(numbers))

# Using reduce to find the sum of squares of triangular numbers in a list
def is_triangular(n):
    x = (8 * n + 1) ** 0.5
    return x.is_integer() and (x - 1) % 2 == 0
def sum_of_squares_of_triangular(numbers):
    return reduce(lambda x, y: x + y * y if is_triangular(y) else x, numbers, 0)    
print("Sum of squares of triangular numbers:", sum_of_squares_of_triangular(numbers))