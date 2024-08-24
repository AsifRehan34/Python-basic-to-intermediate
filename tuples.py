# tuples are ordered and unmutable data types
# they cannot be changed
# they are separated by comma and using paranthesis is optional
a="element1","element2","element3",1,2,3,4

# tuple slicing
# to get the data type
print(type(a))

# to get the element
print(a[0])

# to get element in reverse order

print(a[::-1])

# to get reverse from specific index

print(a[3::-1])
print(a[-2::-1])

# to skip elements

print(a[::3])

# using loops

for i in a:
    print(i)


print()

for i in range(len(a)):
    print(a[i])

print()

i=0
while i>=len(a):
    print(a[i])

# convert tuple to list

a=list(a)
print(a)

print()

a.append("now list")
print(a)

print()

a=tuple(a)
print(a)

# function in tuple

print(a.count(2))

print(a.index("element1"))