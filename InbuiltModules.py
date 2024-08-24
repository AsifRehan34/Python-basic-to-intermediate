# In Python, a module is a file containing Python definitions and statements. Modules are used to break down large programs into smaller, manageable, and organized files. Each module can define functions, classes, and variables, and can also include runnable code. Python has a rich library of inbuilt modules that provide various functionalities to the programmers.

# ibuilt modules

# datetime module
import datetime
# x=datetime.datetime.now()
# print("current date and time is:",x)

# x=datetime.date(2023,3,2)
# print(x)
# x=datetime.time(23,3,2)
# print(x)
# x=datetime.date(1999,7,3)
# print(x.strftime("%D")) #gives date
# print(x.strftime("%A")) #gives day
# print(x.strftime("%Y")) #gives year
# print(x.strftime("%T")) #gives time
# print(x.strftime("%m")) #gives month
# print(x) #gives date

# random
# import random
# x=random.randint(1,6)
# print(x)
#
# list=["kala","pela","neela","chita"]
# x=random.choice(list)
# print(x)

# math
import math
x=math.pow(2,4)
print(x)

print()
x=math.ceil(2.1)
print(x)
print()

x=math.floor(2.7)
print(x)
print()

x=math.sin(90)
print(x)
# Calculate the square root of a number
sqrt_value = math.sqrt(16)
print("Square root of 16:", sqrt_value)

# Calculate the factorial of a number
factorial_value = math.factorial(5)
print("Factorial of 5:", factorial_value)

# Calculate the sine of a number (in radians)
sine_value = math.sin(math.pi / 2)
print("Sine of π/2:", sine_value)
