# While Loop Questions: 

# 1. Find the largest digit in a number. 
# n = int(input("Enter a number : "))
# largest = 0

# while n > 0:
#     digit = n % 10
#     if digit > largest:
#         largest = digit
#     n //= 10

# print("Largest digit is ", largest)

# 2. Find the smallest digit in a number. 
# n = int(input("Enter a number : "))
# smallest = 9

# while n > 0:
#     digit = n % 10
#     if digit < smallest:
#         smallest = digit
#     n //= 10

# print("Smallest digit is ", smallest)

# 3. Count how many even digits are in a number. 
# n = int(input("Enter a number : "))
# count = 0

# while n > 0:
#     digit = n % 10
#     if  digit % 2 == 0:
#         count += 1
#     n //= 10
# print("Number of even digits are : ", count)

# 4. Count how many odd digits are in a number. 
# n = int(input("Enter a number : "))
# count = 0

# while n > 0:
#     digit = n % 10
#     if  digit % 2 != 0:
#         count += 1
#     n //= 10
# print("Number of odd digits are : ", count)

# 5. Create a multiplication table for a given number.  
# n = int(input("Enter a number"))
# i = 1

# while i <= 10:
#     print(i, "X" ,n , "=", i * n)
#     i += 1

# 6. Create a password program that repeatedly asks for a password until the correct password is entered.  
# correct_password = "ilovepython"

# password = input("Enter password :")

# while password != correct_password:
#     print("Incorrect password, Try again")
#     password = input("Enter password : ")

# print("Login successful!")

# 7. Create a student marks program that repeatedly accepts marks until -1 is entered, 
# then displays the total, average, highest mark, lowest mark, and number of students.  
# total = 0
# highest = None
# lowest = None
# count = 0

# while True:
#     mark = int(input("Enter marks : "))
#     if mark == -1:
#         break

#     total += mark
#     count += 1

#     if highest == None or mark > highest:
#         highest = mark

#     if lowest == None or mark < lowest:
#         lowest = mark

# if count > 0:
#     average = total/count

# print("Total marks : ",total)
# print("Number of students : ", count)
# print("Highest marks : ",highest)
# print("Lowest marks : ", lowest)

# For Loop Questions: 

# 1. Print numbers from 10 to 30, but skip numbers divisible by 4.  
# for i in range (10, 31):
#     if i % 4 == 0:
#         continue
#     print(i, end = " ")

# 2. Ask the user for a number and find its factorial. 
# n = int(input("Enter a number : "))

# factorial = 1

# for i in range(1, n+1):
#     factorial *= i
# print("Factorial : ", factorial)

# 3. Ask for a string and print every second character. 
# str = input("Enter a string : ")

# for char in range(1,len(str), 2):
#     print(str[char], end = " ")

# 4. Ask for a string and count vowels and consonants. 
# str = input("Enter a string : ")

# vowels = 0
# consonants = 0

# for char in str:
#     if char in "aeiou":
#         vowels += 1
#     else:
#         consonants += 1

# print("Vowels = ", vowels)
# print("Consonants = ", consonants)

# 5. Ask for a string and check whether it contains only digits. 
# text = input("Enter a string : ")

# only_digits = True

# for char in text:
#     if not char.isdigit():
#         only_digits = False
#         break

# if only_digits:
#     print("String contain only digit")
# else:
#     print("String does not contain only digit")

# 6. Ask for a string and count how many characters are digits, letters, and spaces. 
# text = input("Enter a string : ")
# digit = 0
# letter = 0
# space = 0

# for char in text:
#     if char.isdigit():
#         digit += 1
#     elif char.isalpha():
#         letter += 1
#     elif char == " ":
#         space += 1

# print("Digits = ", digit)
# print("Letters = ", letter)
# print("Spaces = ", space)


# 7. Ask for a string and create its reverse without using slicing, reversed(), lists, or any other data type. 
# text = input("Enter a string : ")
# reverse = " "

# for char in text:
#     reverse = char + reverse

# print("Reverse string is ", reverse)


# 8. Count the number of characters in a string using a for loop. 
# str = input("Enter a string : ")
# letter = 0

# for char in str:
#     if char.isalpha():
#         letter += 1

# print("Number of characters : ", letter)

# 9. Count the number of vowels in a string. 
# text = "Python is a programming language"
# vowels = 0

# for char in text:
#     if char in"aeiou":
#         vowels += 1
# print("Vowels = ", vowels)

# 10. Count the number of spaces in a string.  
# text = "Python is a programming language"
# space = 0

# for char in text:
#     if char == " ":
#         space += 1
# print("Number of spaces = : ",space)

# 11. Reverse a string using a for loop. 
# str = input("Enter a string : ")
# reverse = " "

# for char in str:
#     reverse = char + reverse
# print("Reverse string is ", reverse)

# 12. Check whether a string is a palindrome using a for loop. 
# text = input("Enter a string :")

# reverse = ""
# for char in text:
#     reverse = char + reverse

# if text == reverse:
#     print("Text is palindrome")
# else:
#     print("Text is not palindrome")

# 13. Count the number of occurrences of each vowel (a, e, i, o, u).
# text = input("Enter a string : ")

# a_count = 0
# e_count = 0
# i_count = 0
# o_count = 0
# u_count = 0

# for char in text.lower():
#     if char == 'a':
#         a_count += 1
#     elif char == 'e':
#         e_count += 1
#     elif char == 'i':
#         i_count += 1
#     elif char == 'o':
#         o_count += 1
#     elif char == 'u':
#         u_count += 1

# print( "Count of a : ", a_count)
# print( "Count of e : ", e_count)
# print( "Count of i : ", i_count)
# print( "Count of o : ", o_count)
# print( "Count of u : ", u_count)
    