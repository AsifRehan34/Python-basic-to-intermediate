# function are block of code that is reusable
# makes the code easy to test and debug
# easy to manage
# in python def is used to define the function followed by the variable ,which is the name of the variable ,followed by the brackets
# then starts the body of the function where our main logic of the function is written
# the we call the function by its name

# def add():
#     a=3
#     b=4
#     print(a+b)
# add()

# Parameters and Arguments
# parameters are the variables written inside the brackets while defining a function
# arguments are the values that are parsed into the function while calling it

# def add(a,b):
#     print(a+b)
# add(3,4)

# Return
# similary we can use return which stores the values of the function and ends it

# def add(a,b):
#     return (print(a+b))
# add(4,5)

# recursive functions
# recursive functions are used where recursion or loop of the data is necessary without using loops
# the function calls itself again and again . in python its limit is defined and after that it will through an error
# def add(a,b):
#     print(a+b)
#     return (add(a,b))
# add(5,5)

# print a factiorial using recursion
# def fact(a):
#     if a==1:
#         return 1
#     else:return (a *fact(a-1))
#
# x = int(input("enter a number:"))
# print(fact(x))

# arbitrary arguments
# multiple arguments de skte hn in the form tuple
# def func(*a):
#     print("my name is:",a[0])
#     return
# func("rehan","kashan","sultan")

# local and global variable: just inside a block of code declared global can be used anywhere
# a=2
# def add():
#     global a
#     a=3
#     b=4
#     print(a+b)
# add()
# print(a)

# lamda function :a temproray function that stores value for a period of time,not in the memory
    # can take multple arguments but single expression
# a=lambda v:v*5
# print(a(5))

# a=lambda x,y,z:(x-y)*z
# print(a(4,5,5))


# febonacii series element at specific index
# def febo(num):
#     if num==1:
#         return 0
#     elif num==2:
#         return 1
#     # for i in range (1,8):
#     else:return (febo(num-1)+febo(num-2))
# print(febo(7))
