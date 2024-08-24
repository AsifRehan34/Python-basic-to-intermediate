# dictionary is used to store data in the form of keys and value
# dictionary is enclosed in {} braces
# every key value is separated by colon
# every key value pair is separated by ,

# a={"Name":"John","StudID":20,"age":30}
# print(type(a))
# print(a["Name"])
#
#
# print()
#
# print(a.items())
#
# print()
#
# print(a.values())
#
# print()
#
# print(a.get("age"))
# print()
# for i in a:
#     print(i)
#
# print()
# for i in a:
#     print(a[i])
#
# print()
# for x in a.values():
#     print(x)
#
# print()
#
# for x,y in a.items():
#     print(x,":",y)
#
# b=a.items()
# print(b)
#
# print()
#
# c=a.values()
# print(c)
#
# print()
#
# d=a.copy()
# print(d)
#
# a.pop("age")
# print(a)
# print()
# a.setdefault("age",40)
# print(a)
#
# print()
# b={"Name":"Asif","age":25}
# a.update(b)
# print(a)
# print()


# updating with list items
# list1=[('age',40)]
# a.update(list1)
# print(a)
# print()

# updating with keyword arguments
# a.update(age=20)
# print(a)

# clearing dictionary
# a.clear()
# print(a)

# returns the key value pair in lifo:last in first out ,the item that was poped from dictionary
# b=a.popitem()
#
# print("this item",b)

# Nested dictionary

# dictionary={1:{"Name":"Asif","Age":25,"Bloogroup":"B+"},
#             2:{"Name":"Rehan","Age":24,"Bloogroup":"A+"},
#             3:{"Name":"Malik","Age":27,"Bloodgroup":"O-"}}
# print(dictionary)

# print(dictionary[2])
# print(dictionary[3]["Name"])