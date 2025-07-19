import math
def calculate_square_root(num):
    return math.sqrt(num)
def natural_algorithm(num): 
    return num ** 0.5
def sine(num):  
    return math.sin(num)

print("Enter a number:")
number = int(input())

print(f"The square root of {number} is {calculate_square_root(number)}")
print(f"The natural algorithm of {number} is {natural_algorithm(number)}")
print(f"The sine of {number} is {sine(number)}")  