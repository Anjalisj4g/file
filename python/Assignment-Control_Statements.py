'''Conditional Statements
1. What Should I Eat? You are ordering food with your friends. 
Your choice depends on your preference. 
● If you choose 1, order pizza. 
● If you choose 2, order a burger. 
● If you choose 3, order noodles. 
● Otherwise, display "Choice not available.'''

# choice = int(input("Choose a food item :"))

# if choice == 1:
#     print("order = pizza")
# elif choice == 2:
#     print("order = burger")
# elif choice == 3:
#     print("order = noodles")
# else:
#     print("Choice not available")

'''2. How Should I Travel to School? 
You are getting ready for school and need to decide how to travel. 
● If the distance is less than 1 km, walk. 
● If the distance is between 1 and 5 km, take a bicycle. 
● If the distance is more than 5 km, take the bus. '''

# distance = float(input("Choose the distance to school : "))

# if distance < 1:
#     print("Walk")
# elif 1 < distance <5:
#     print("Take a bicycle")
# elif distance > 5:
#     print("Take the bus")
# else:
#     print("Incorrect input")

'''3. Can I Buy It? You see a pair of headphones that you really want to buy. 
The program should check: 
1. Whether you have enough money. 
2. If you have enough money, check whether you actually want the headphones. 
3. If both conditions are satisfied, you can buy them. '''

# avai_money = float(input("Available money : "))
# head_p = float(input("Headphone price : "))
# need = input("Wants the item(Yes/No) : ")

# if head_p <= avai_money and need == "Yes":
#     print("Buy the head phone")
# else:
#     print("Don't buy the head phone")

'''4. Ordering Food With Friends 
You and your friends are ordering food. 
First, ask whether the restaurant is open. 
● If it is closed → display "Let's choose another restaurant." 
● If it is open, ask whether vegetarian food is required. ○ If yes → suggest a vegetarian meal. 
○ Otherwise → suggest a regular meal. '''

# restaurant = input("Choose if the restaurant is open or close(open/close) : ")


# if restaurant == "open":
#     veg_available = input("Vegetarian meal available(Yes/No) : ")
#     if veg_available == "Yes":
#         print("Suggest a vegetarian meal")
#     else:
#         print("Suggest a regular meal")
# else:
#     print("Let's choose another restaurant")


'''5. What Should I Wear Today? 
You are getting ready to go outside. 
Based on the temperature: 
● Below 15°C → Wear a jacket. 
● 15–25°C → Wear comfortable clothes. 
● 26–35°C → Wear light clothes. 
● Above 35°C → Stay cool and drink plenty of water. '''

# temp = float(input("Choose the temperature(in degree celcius) :"))

# if temp < 15:
#     print("Wear a jacket")
# elif 15 < temp < 20:
#     print("Wear comfortable clothes")
# elif 26 < temp < 35:
#     print("Wear light clothes")
# elif temp > 35:
#     print("Stay cool and drink plenty of water")
# else:
#     print("Invalid input")

'''6. Game Tournament Entry 
Your school is organizing a gaming tournament. 
To enter: 
● The student must be at least 12 years old. 
● If they are old enough, check whether they have registered. 
● Registered students can participate. 
● Students who haven't registered should be asked to register first. '''

# age = int(input("Student's Age : "))

# if age >=12:
#     reg_status = input("Whether the student already registered(Yes/No) : ")
#     if reg_status =="Yes":
#         print("Student can participate")
#     else:
#         print("Register first for participating")
# else:
#     print("Not eligible to participate")

'''7. “Do I Have Enough Money for Ice Cream?” 
You are at an ice-cream shop with ₹100 in your pocket. 
Ask the user for the price of the ice cream. 
● If they have enough money, they can buy it. 
● Otherwise, they need to save their money. '''

# price = int(input("Price of ice-cream : "))

# if price < 100:
#     print("Buy ice-cream")
# else:
#     print("Don't buy ice-cream, let's save money")

'''8. “What Drink Should I Get?” 
You are at a café with your friends. 
Give the user these choices: 1. Juice 2. Milkshake 3. Soft drink 4. Water 
The program should display the selected drink. 
If the user enters anything else, display "Invalid choice." '''

# print("Choose from the given list: 1. Juice 2. Milkshake 3. Soft drink 4. Water")

# drink = int(input("Enter your choice : "))

# if drink == 1:
#     print("Juice")
# elif drink == 2:
#     print("Milkshake")
# elif drink == 3:
#     print("Soft drinks")
# elif drink ==4:
#     print("Water")
# else:
#     print("Invalid choice")

'''9. “Study or Watch Netflix?” 
You have an exam tomorrow. Ask: 
● Is there an exam tomorrow? 
● How much of the syllabus is completed? Rules: 
● No exam tomorrow → "Enjoy your free time!" 
● Exam tomorrow + less than 80% completed → "Study first!" 
● Exam tomorrow + 80% or more completed → "You can take a short break." '''

# exam = input("Is there an exam tomorrow ?(Yes/No) ")

# if exam == "Yes":
#     completed = int(input("How much syllabus is completed ?(in %)"))
#     if completed < 80:
#         print("Study first")
#     else:
#         print("You can take a short break")
# else:
#     print("Enjoy your free time!")

'''10. “The Shop Is Closing!” 
You are at a shop with your friends. Ask for the current time. 
● Before 8 PM → "You still have time to shop." 
● 8–9 PM → "Hurry! The shop is closing soon." 
● After 9 PM → "The shop is closed." '''

# time = float(input("What's the time ?"))

# if time < 8:
#     print("You still have time to shop.")
# elif 8 < time < 9:
#     print("Hurry! The shop is closing soon.")
# elif time >9:
#     print("The shop is closed.")
# else:
#     print("Inavalid input")