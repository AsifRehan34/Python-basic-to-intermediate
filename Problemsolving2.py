# check if a number is positive

# number = int(input("Enter a number:"))
# if number >= 0: print("Number is postive!")

# check weather number is even or odd

# number = int(input("Enter a number:"))
# if number%2==0: print("Number is even")
# else: print("Number is odd")

# calculating area

# length = int(input("Enter the length:"))
# width = int(input("Enter the width:"))
#
# area=length *width
# print("Area is :",area)

# letter= input("Enter a letter:")
# if letter  in ('aeiou') :
#     print("vowel")
# else:
#     print (" not vowel")

number = int(input("enter a number:"))
if number in range(0, 10):
    print("single digit")
elif number in range(10, 100):
    print("2 digit number")
elif number in range(100, 1000):
    print("3 digit number")
elif number in range(1000, 10000):
    print("4 digit number")
else:
    print("more than 4 digit number")
