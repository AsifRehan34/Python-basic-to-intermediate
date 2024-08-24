# set are unordered and mutable datatypes
# they are enclosed in curly brackets
# they are unique and cant store repeatable value


a={"a","b","c","d","e","f","g"}
b={"g","h"}
c={"c","d","e","f","g","h","i","j","k"}

# printing type
# print(type(a))
#
# print()

# iterating through set elements
# for i in a:
#     print(i)
# print()

# functions of sets

# to add a new value
# c.add("l")
# print(c)
# print()

# to pop any value
# a.pop()
# print(a)
# print()

# to remove specific value
# b.remove("f")
# print(b)
# print()
# to discard specific value work same as remove
# c.discard("l")
# print(c)
# print()

# to update set a with set b meaning common values will be discarded and new value will be added to a

# a.update(b)
# print(a)
#
# print()

# we can negate/diffrentiate value b from value of a. or the elements that are present in set a but not in c
# x=a.difference(c)
# print(x)
# #
# print()

# minus the other set values and update the first set
# a.difference_update(b)
# print(a)

# to print common values
# print(a.intersection(b))

# to print whole a,b values discarding repeating valeus

# print(a.union(b))

# disjoint means no repeating values
# print(a.isdisjoint(b))

# subset means set b contains all the values that are present in set c
# print(b.issubset(c))

# super set means c contains all the values present in b
# print(c.issuperset(b))

# intersection update keeps the element present in either of sets
# c.intersection_update(b)
# print(c)

# present in either of sets but not in their intersection
# d=b.symmetric_difference(a)
# print(d)