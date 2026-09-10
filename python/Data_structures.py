'''Selection Sort'''
# numbers = [34,67,84,18,90,25]

# n = len(numbers)

# for i in range(n):
#     min_index = i

#     for j in range(i + 1, n):
#         if numbers[j] < numbers[min_index]:
#             min_index = j

#         numbers[i], numbers[min_index] = numbers[min_index],numbers[i]
# print(numbers)

'''Bubble Sort'''
# numbers = [23,56,12,86,10]
# n = len(numbers)

# for i in range(n):
#     for j in range(0, n - i - 1):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
# print(numbers)

'''Optimised Bubble sort'''

# numbers = [34,21,57,30,31,87]
# n = len(numbers)

# for i in range(n):
#     swapped = False

#     for j in range(0, n - i - 1):

#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

#     swapped = True

# print(numbers)

'''Searching'''
'''Linear Search'''

# numbers = [21, 30, 31, 34, 57, 87]

# target = 34

# Found = False

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         Found = True
#         break

# if Found:
#     print("Number found")
# else:
#     print("Number not found")

'''Linear search with index'''
# numbers = [21, 30, 31, 34, 57, 87]

# target = 30

# for i in range(len(numbers)):

#     if numbers[i] == target:
#         print("Number found at index ", i)
#         break
# else:
#         print("Number not found")

'''Binary Search'''
# number = [10,27,57,71,73,85,94]

# target = 85
# low = 0
# high = len(number) - 1

# found = False

# while low <= high:
#     mid = (high + low) // 2

#     if number[mid] == target:
#         found = True
#         break

#     elif number[mid] < target:
#         low = mid + 1

#     else:
#         high = mid - 1

# if found:
#     print("Element found at index", mid)
# else:
#     print("Element not found")

