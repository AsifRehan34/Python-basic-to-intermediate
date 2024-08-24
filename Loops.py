# for loops

# for i in range(1,6,2):
#     print(i)

# for i in range (1,11):
#     n=i*7;
#     print("7 *",i,":",n)

# while loops
# numb=int(input("Input a number:"))
# i=0
# while i<=10:
#     tab=numb*i
#     print(tab)
#     i = i + 1

# a=int(input("enter a number for table"))
# b=int(input("enter range:"))
# i=1
# while i in range(1,b+1):
#     print(a ,"*",i,i*a)
#     i=i+1

# while True:
#     x=int(input("enter a number:"))
#     y=int(input("enter 2nd number:"))
#
#     print(x**y)
#
#     user=input("do u want to continue:")
#     if user=="no":
#         break


# nested loops

# for i in range(1,6):
#     for j in range(1,6):
#         if j<=i:
#             print("* " ,end="")
#             j+=1
#
#     print()
#     i+=1
#
# for i in range (1,6):
#     for j in range(5,i,-1):
#         print(" ",end=" ")
#     for k in range (i):
#         print("*", end=" ")
#     print()
#
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()
#
#     1
#     21
#     321
#     4321
#     54321
# how this works
#     for i=1:
#         j=1
#         print(1)
#     for i=2
#         j=2
#         print(2)
#         j=1
#         print(1)

#
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print()
# for k in range(5,1,-1):
#     for l in range(k,1,-1):
#         print("*",end=" ")
#     print()
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(1,9):
#     for j in range(1,i+1):
#         print(j*i,end=" ")
#     print()
#
# 1
# 2 4
# 3 6 9
# 4 8 12 16 
# 5 10 15 20 25
# 6 12 18 24 30 36
# 7 14 21 28 35 42 49
# 8 16 24 32 40 48 56 64