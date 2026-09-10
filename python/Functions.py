# def greet():
#     print("Hello")

# greet()

# def add(a, b):
#     print(a + b)

# add(20, 30)
# add(9, 10)
# add(12, 98)

# def greet(name):
#     print("Hello", name)

# greet("Anjali")    

# def add(a, b):
#     return a + b

# result = add(10, 20)
# print(result)

# print(result * 2)

# def calculate_total(price, quantity):
#     return price * quantity

# result = calculate_total(200,5)
# print(result)

# def calculate(price, discount):
#     return price - (price * discount/100)

# total = calculate(1000,23)
# print(total)

'''Positional Arguments'''
# def student(name, age):
#     print(name, age)

# student("Susan", 40)

# def divide(a, b):
#     return a/b

# print(divide(10,2))

'''Keyword Argument'''
# def student(name, age):
#     return name, age

# print(student(age = 20, name = "Ashwin"))

'''Default Argument'''
# def greet(name = "Raju"):
#     print("Hello" + " " + name)

# greet()

# def calculate(distance, rate = 10):
#     return distance * rate

# print(calculate(20))
# print(calculate(15))
# print(calculate(12,8))

'''Variable Length Argument'''
'''*args'''

# def add(*num):
#     return sum(num)

# print(add(10,20,30))


# def display(*nums):
#     return nums

# print(display(1,2,3,4,5,6,7,8,9,10))

'''**kwargs'''
# def dic(**details):
#     print(details)

# dic(Ambu = 23, Kashi = 20, Appu = 25)

'''Local Variable'''
# def greet():
#     name = "Anu"
#     print(name)
# greet()

# def greet():
#     name = "Anu"
#     print(name)
# greet()
# print(name)

# name = "Anu"
# def greet():
#     print(name)
# greet()

# name = "Anu"
# def greet():
#     print(name)
# greet()
# print(name)

# name = "Anu"
# def greet():
#     name = "Hari"
#     print(name)
# greet()
# print(name)

# x = 100
# def test():
#     x = 50
#     print(x)

# test()
# print(x)

'''Global keyword'''
# count = 100
# def calculate():
#     global count
#     count = 50
#     print(count)
# calculate()
# print(count)

'''Nested function'''
# def outer():
#     def inner():
#         print("Inside")

#     inner()
#     print("outside")
# outer()

# def outer():
#     print("Outside")

#     def inner():
#         print("Inside")

#     inner()
# outer()

'''Lambda function'''
# square = lambda x : x * x
# print(square(6))

# add = lambda a, b : a+b
# print(add(20,30))

# check = lambda x : "even " if x % 2 == 0 else "odd"
# print(check(34))

# numbers = [1,2,3,4,5]
# result = map(lambda x : x*x, numbers)
# print(list(result))

# result1 = map(lambda x: x**5, numbers)
# print(list(result1))

# numbers = [1,2,3,4,5]
# result = filter(lambda x : x%2 == 0, numbers)
# print(list(result))

'''Recursive Function'''
'''Factorial'''

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(6))

# def countdown(n):
#     if n == 0:
#         return

#     print(n)

#     countdown(n - 1)

# print(countdown(5))
    
'''Fibonacci Using Recursion'''
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(7)) 

# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

# for i in range(7):
#     print(fibonacci(i))


'''Practice Questions'''
'''Student Result'''
# def calculate_average(mark1, mark2, mark3):
#     total = mark1 + mark2 + mark3
#     average = total / 3
#     return average

# marks = [80, 67, 92]

# average = calculate_average(
#     marks[0],
#     marks[1],
#     marks[2]
# )
# print("Average marks : ", average)

'''Create a simple ATM using functions'''

# balance = 5000
# def check_balance():
#     print("Available balance : ", balance)

# def deposit(amount):
#     global balance
#     balance += amount
#     print("Amount Deposited : ", amount)

# def withdraw(amount):
#     global balance
#     if amount <= 0:
#         print("Incorrect credential")
#     elif amount <= balance:
#         balance -= amount
#         print("Amount withdrawn : ", amount)
#     else:
#         print("Insufficient credential")

# check_balance()
# deposit(500)
# withdraw(2000)
# check_balance()

# '''Login System'''
# def login(user_name, password):
#     if user_name == "admin" and password == "1234":
#         return True
#     else:
#         return False

# user_name = input("Enter a user name : ")
# password = input("Enter password : ")

# if login(user_name, password):
#     print("Login successful")
# else:
#     print("Invalid credential")