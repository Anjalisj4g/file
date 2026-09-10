'''extract the phone number'''

# import re

# text = "My phone number is 987654321"

# result = re.search(r"\d+",text)

# print(result.group())

'''re.search'''
# import re

# text = "python programming"

# result = re.search("python", text)

# if result:
#     print("Found")

# else:
#     print("Not found")

'''re.match'''
# import re

# text = "Python is a programming language"
# result = re.match("Python", text)

# if result:
#     print("found")
# else:
#     print("Not found")


# import re

# text = "Python is a programming language"
# result = re.match("programming", text)

# if result :
#     print("Found")
# else:
#     print("Not found")

'''re.findall'''
# import re

# text = "I have 10 apples and 20 oranges"

# result = re.findall(r"\d+",text)

# print(result)

'''re.sub'''
# import re

# text = "python is a programming language"

# result = re.sub("programming", "object-oriented", text)
# print(result)

'''Email Validation'''
# import re

# email = "company@gmail.com"
# pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

# if re.match(pattern, email):
#     print("Valid email")
# else:
#     print("Invalid email")

'''os module'''

'''Get Current Working Directory'''
# import os
# print(os.getcwd())

'''change directory'''
# import os
# print(os.chdir("C:\\Users\\Anjali\\Documents"))

'''List Files and Folders'''
# import os
# print(os.listdir())

'''Create a Directory'''
# import os
# print(os.mkdir("Report"))

'''Create Nested Directories'''
# import os
# print(os.makedirs(data/2016/jan))

'''Remove a file'''
# print(os.remove(data.txt))

'''Remove a Directory'''
# print(os.rmdir())

'''Check Whether File Exists'''
# if os.path.exists("file.txt"):
#     print("Exist")
# else:
#     print("Not exist")

'''Working with Paths'''
# os.path.join("Documents", "data.csv")

'''Exceptional Handling'''
# try:
#     a = 10
#     b = 0
#     result = a / b
#     print(result)

# except ZeroDivisionError:
#     print("Cannot divide by 0")

# try:
#     n = int(input("Enter a number : "))
#     result = 10/n
#     print(result)

# except ValueError:
#     print("Enter a valid number")

# except ZeroDivisionError:
#     print("Cannot divide by Zero")


# try:
#     n = int(input("Enter a number : "))
#     result = 10/n

# except ZeroDivisionError:
#     print("Cannot divide by Zero")

# else:
#     print("Result : ",result)


# try:
#     n = int(input("Enter a number : "))
#     result = 10/n

# except ZeroDivisionError:
#     print("Cannot divide by Zero")

# else:
#     print("Result : ",result)

# finally:
#     print("Program execution completed")

'''raise'''
# age = 15

# if age < 18:
#     raise ValueError("Age must be greater than or equal to 18")

'''User-defined Exception'''
# class InsufficientBalanceError(Exception):
#     pass

# balance = 1000
# withdraw = 2000

# try:
#     if withdraw > balance :
#         raise InsufficientBalanceError("Insufficient Balance")

# except InsufficientBalanceError as e:
#     print(e)

'''Exception Object using as'''
# try:
#     number = int("abc")
# except ValueError as e:
#     print(e)

