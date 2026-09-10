# class Addition:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def add(self):
#         print(self.a + self.b)

# obj = Addition(20, 30)
# obj.add()

'''Creating class and object'''
# class Student:
#     name = "Surya"
#     age = 23

# student1 = Student()

# print(student1.name)
# print(student1.age)

'''Create an Employee class that accepts name and salary 
through the constructor and displays them.'''

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display(self):
#         print("Name : ", self.name)
#         print("Salary : ", self.salary)

# employee1 = Employee("Anjali", 30000)
# employee1.display()

# employee2 = Employee("Gokul",50000)
# employee2.display()

'''Create a Rectangle class with length and width, 
and create a method area() that returns the area.'''

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# rectangle1 = Rectangle(5, 10)
# print("Area = ", rectangle1.area())


'''Create a Car class with:
1. brand
2. model
Then create 3 different car objects and display their details.'''

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def display(self):
#         print("Brand name : ", self.brand)
#         print("Model name : ", self.model)

# car1 = Car("Toyota", "Fortuner")
# car2 = Car("Honda", "City")
# car3 = Car("BMW", "X5")

# car1.display()
# car2.display()
# car3.display()

'''Encapsulation'''

'''Create a BankAccount class with:
private variable __balance
deposit(amount)
withdraw(amount)
display_balance()
The user should not be able to directly access __balance.'''

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount
#         print("Amount deposited : ", amount)

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient Balance")

#     def display_balance(self):
#         print("Balance = ", self.__balance)


# account1 = BankAccount(5000)

# account1.display_balance()

# account1.deposit(2000)

# account1.withdraw(3000)

# account1.display_balance()

'''Inheritance'''

'''Create a parent class Animal with a method sound().
Create a child class Dog that inherits from Animal and overrides the sound() method.'''

# class Animal:

#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):

#     def sound(self):
#         print("Dog barks")

# dog1 = Dog()
# dog1.sound()

'''Method Overriding'''

'''Create:
A parent class Vehicle
A method start() that prints "Vehicle starts"
A child class Car
Override start() in Car to print "Car starts with a key"'''

# class Vehicle:

#     def start(self):
#         print("Vehicle starts")

# class Car(Vehicle):

#     def start(self):
#         print("Car starts with a key")

# car1 = Car()
# car1.start()

'''super() in Inheritance'''

'''Create:
Parent class Person with name
Child class Student with name and course
Use super() to initialize name'''

# class Person:

#     def __init__(self, name):
#         self.name = name

# class Student(Person):

#     def __init__(self, name, course):
#         super().__init__(name)
#         self.course = course

#     def display(self):
#         print("Name : ", self.name)
#         print("Course : ", self.course)

# student1 = Student("Karthik", "Data Science")

# student1.display()

'''Polymorphism'''

'''Create two classes:
Dog → sound() prints "Dog barks"
Cat → sound() prints "Cat meows"
Then create a function that accepts an object and calls its sound() method.'''

# class Dog:

#     def sound(self):
#         print("Dog barks")

# class Cat:

#     def sound(self):
#         print("Cat meows")

# def make_sound(animal):
#     animal.sound()

# dog1 = Dog()
# dog1.sound()

# cat1 = Cat()
# cat1.sound()

'''Create a BankAccount class that:
Stores account holder name, account number, and balance.
Uses a constructor to initialize the values.
Keeps balance private using __balance.
Has a deposit() method.
Has a withdraw() method.
Has a check_balance() method.
Prevents withdrawal when the amount is greater than the balance.'''

# class BankAccount:
#     def __init__(self, name, account_number, balance):
#         self.name = name
#         self.account_number = account_number
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print("Amount deposited : ", amount)
#         else:
#             print("Invalid amount")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Invalid credential")
#         elif amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient balance")

#     def check_balance(self):
#         print("Account Holder : ", self.name)
#         print("Account number : ", self.account_number)
#         print("Balance : ", self.__balance)

# account1 = BankAccount("Anjali", 123456789, 5000)

# account1.check_balance()

# account1.deposit(308)

# account1.withdraw(500)

# account1.check_balance()
