# list are ordered and mutable datatypes
# mutable means list once created can be changed and manipulated
# ordered means they follow indexing
# they are separated by commas and written inside square brackets

# string slicing

# list=["alpha","beta","gamma",1,2,3,4,5,6]
#
# print(list)
# print(list[:2])
# print(list[1:3])
# print(list[::-1])
# print(list[::2]) #skips every element at the range given
# print(list[-1:-8:-1])

# list itration

# iteration using for loop
# a=["alpha","beta","gamma",1,2,3,4,5,6]
# for i in range(len(a)):
#     print(a[i])

# i=0
# while i<len(a):
#     print(a[i])
#     i+=1

# [print (i) for i in a] #short hand for loop

# list functions

# 1. find length of list
# print(len(a))
# 2. find occurence of an element
# print(a.count(1))
# 3. add elememt to list
# a.append("appending")
# print(a)
# add element to specific location
# a.insert(2,"appending ")
# print(a)
# 4.remove element from list
# a.remove("appending")
# print(a)
# 5. to remove from certain location
# a.pop(3)
# print(a)

# # copy of list
# a=[1,3,4,5,6,7]
# b=a.copy()
# print(b)
# # access an element
# print(a.index(4))
# # to extend the list
# b=[8,9,10,11,12]
# a.extend(b)
# print(a)
#
# # to reverse the list
# a.reverse()
# print(a)
#
# # sort list
# a.sort()
# print(a)
# # clear all the data from list
# print(a)
# a.clear()

# list comprehension

l1=[2,4,7,8,9,22]
l2=[]
for i in l1:
    if i>7:
        l2.append(i)
print(l2)

# same code can be written as
l3=[i for i in l1 if i>7]
print(l3)