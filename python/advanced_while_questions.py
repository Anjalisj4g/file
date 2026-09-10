# 1. Print even numbers from 2 to 20 using a while loop. 
# i = 2
# print("Even numbers from 2 to 20 are ", end = " ")
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end = " , ")
#     i += 1

# 2. Check if a number is Armstrong or not. 
# n = int(input("Enter a number : "))

# temp = n
# digits = len(str(n))
# total = 0

# while temp > 0:
#     digit = temp % 10
#     total = total + digit**digits
#     temp //= 10

# if total == n:
#     print("Armstrong")
# else:
#     print("Not armstrong")

# 3. Check whether a given number is a palindrome using a while loop. 
# (e.g., 121 → 121 = Palindrome, 123 → 321 = Not Palindrome) 
# (e.g., malayalam → Palindrome,  english→(hsilgne) Not Palindrome) 
# n = int(input("Enter a number : "))

# original = n
# reverse = 0

# while n > 0 :
#     digit = n % 10
#     reverse = reverse*10 + digit
#     n //= 10

# if original == reverse:
#     print("Palindrome")
# else:
#     print("Not palindrome")

# 4. Count the number of digits in a given number using a while loop. 
# n = int(input("Enter a  number : "))

# count = 0
# while n > 0:
#     count += 1
#     n //= 10

# print("Number of digits : ", count)

# 5. Find the largest digit in a given number using a while loop. 
# n = int(input("Enter a number :"))
# lar = 0
# while n > 0:
#     digit = n % 10
#     if digit > lar:
#         lar = digit
#     n //= 10
# print("Largest digit is ", lar)

# 6. Print the sum of even and odd digits separately in a number. 
n = int(input("Enter a number : "))
even_sum = 0
odd_sum = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit

    n //= 10

print("Sum of even numbers : ", even_sum)
print("Sum of odd numbers : ", odd_sum)