'''for loop'''

# thislist = ["Apple", "Banana", "Grapes"]
# for x in thislist:
#     print(x)

# for i in range(len(thislist)):
#     print(thislist[i])

# [print(x) for x in thislist]

'''While loop'''

# thislist = ["Apple", "Banana", "Grapes"]
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i = i + 1

'''List comprehension'''
# thislist = ["Apple", "Banana", "Grapes"]
# new_list = []

# for x in thislist:
#     if 'a' in x:
#         new_list.append(x)
# print(new_list)

# thislist = ["Apple", "Banana", "Grapes"]
# new_list = [x for x in thislist if 'a' in x]

# print(new_list)

# list1 = [x for x in range(10) if 1 < x < 6]
# print(list1)

# thislist = ["Apple", "Banana", "Grapes"]
# list1 = ["Hello" for x in thislist]
# print(list1)

# thislist = ["Apple", "Banana", "Grapes"]
# list2 = [x if x != 'Banana' else 'Orange' for x in thislist]
# print(list2)

# thislist = ["Apple", "Banana", "Grapes"]
# thislist.sort()
# print(thislist)

# thislist = ["Apple", "Banana", "Grapes"]
# thislist.sort(reverse = True)
# print(thislist)

'''Making copies'''
# thislist = ["Apple", "Banana", "Grapes"]
# list3 = thislist.copy()
# print(list3)

# list4 = list(thislist)
# print(list4)

# list5 = thislist[:]
# print(thislist)

'''Join lists'''

# list1 = ["Apple", "Banana", "Grapes"]
# list2 = ["Pineapple", "Orange", "Pomegranate"]
# print(list1 + list2)

# for x in list2:
#     list1.append(x)
# print(list1)

# list1.extend(list2)
# print(list1)