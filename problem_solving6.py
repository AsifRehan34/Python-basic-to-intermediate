# a={1,4,45,9,3,50}
# large=1
# for i in a:
#     if i>large:
#         large=i
# print(large)

# print()

# a={1,4,45,9,3,50}
# min=50
# for i in a:
#     if i<min:
#         min=i
# print(min)

# print()
# print(max(a))
#
# print()
# print(min(a))

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

# Common elements:
# - 3, 4, and 5 are common between list1 and list2.
# - 5 is common in all three lists.
# - 6 and 7 are common between list2 and list3.
print(set(list1) & set(list2) & set(list3))