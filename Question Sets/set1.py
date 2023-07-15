#1

print("Hello, World!")

#2

my_integer = 10
my_float = 3.14
my_string = "Hello, World!"
my_boolean = True
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_dictionary = {"name": "John", "age": 25, "country": "USA"}
my_set = {1, 2, 3, 4, 5}

#3

# Create a list of numbers from 1 to 10
my_list = list(range(1, 11))
print("Original list:", my_list)

# Add a number to the list
my_list.append(11)
print("After adding 11:", my_list)

# Remove a number from the list
my_list.remove(3)
print("After removing 3:", my_list)

# Sort the list in ascending order
my_list.sort()
print("After sorting in ascending order:", my_list)

#4

def calculate_sum(numbers):
    total_sum = sum(numbers)
    return total_sum

def calculate_average(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return average

numbers_list = [10, 20, 30, 40, 50]

# Calculate the sum of the numbers
sum_of_numbers = calculate_sum(numbers_list)
print("Sum of the numbers:", sum_of_numbers)

# Calculate the average of the numbers
average_of_numbers = calculate_average(numbers_list)
print("Average of the numbers:", average_of_numbers)

#5

def reverse_string(input_string):
    return input_string[::-1]

input_string = "Hello, World!"
reversed_string = reverse_string(input_string)

#6

def count_vowels(input_string):

    input_string = input_string.lower()

    vowels = {'a', 'e', 'i', 'o', 'u'}

    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

#7

def is_prime(number):
    
    if number <= 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

#8

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
#9

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        return fib_sequence

#10

squares_list = [x**2 for x in range(1, 11)]
print(squares_list)
