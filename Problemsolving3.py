# fibonacci series

# a=0
# b=1
# for i in range (0,10):
#     print(a)
#     c=a
#     a=b
#     b=c+a    # print(b)


# def fibonacci(n):
#     a = 0
#     b= 1
#     for i in range(n):
#         print(a, end=' ')
#         a= b
#         b= a + b
#
# # Example usage:
# n = 10  # Number of terms in the Fibonacci series
# fibonacci(n)

# prime numbers
# number=int(input("enter a number to check if its prime:"))
# if number==1:
#     print("Number should be greater than one")
# else:
#     for i in range(2,number):
#         if number%i==0:
#             print("not prime")
#             break
#     else: print("prime")


# palindrome

number=int(input("Enter a number:"))
temp=number
reverse=0
while number>0:
    digit=number%10
    reverse=reverse*10+digit
    number=number//10
if reverse==temp:
    print("palindrome")
else:    print("not palindrome")
