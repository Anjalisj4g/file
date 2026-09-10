'''read()'''
# file = open(r"C:\Users\gokul\OneDrive\Desktop\QIS\python\new.txt",mode = "r")
# content = file.read()
# print(content)
'''readline()'''
# file = open(r"C:\Users\gokul\OneDrive\Desktop\QIS\python\new.txt", "r")
# print(file.readline())

# file = open(r"C:\Users\gokul\OneDrive\Desktop\QIS\python\new.txt", "r")
# print(file.readline())
# print(file.readline())

'''readlines'''
# file = open(r"C:\Users\gokul\OneDrive\Desktop\QIS\python\new.txt", "r")
# print(file.readlines())

# file = open(r"C:\Users\gokul\OneDrive\Desktop\QIS\python\new.txt", "r")
# content = file.readlines()
# print(content[2])
'''write'''
# file = open(r"C:\Users\gokul\OneDrive\Desktop\QIS\python\new.txt",mode = "w")
# content = file.write("Hello")
# file.close()

# file = open(r"C:\Users\gokul\OneDrive\Desktop\QIS\python\new.txt",mode = "w")
# file.write("hi")
# file.write("\nhello")
# file.write("\nhow are you")
# file.close()

'''writelines'''
# skills = ["Data Science", "\nMachine Learning","\nDeep Learning"]
# file = open(r"C:\Users\gokul\OneDrive\Desktop\QIS\python\new.txt",mode = "w")
# file.writelines(skills)
# file.close()

# file = open(r"C:\Users\gokul\OneDrive\Desktop\QIS\python\new.txt",mode = "w")
# file.writelines(["Python\n", "Power BI\n", "SQL"])
# file.close()

# file = open(r"C:\Users\gokul\OneDrive\Desktop\QIS\python\new.txt",mode = "r")
# content = file.read()
# print(content)

'''seek'''
# file = open(r"C:\Users\gokul\OneDrive\Desktop\QIS\python\new.txt",mode = "w+")
# content = file.write("Hi")
# file.seek(0)
# print(file.read())
# file.close()

# file = open(r"C:\Users\gokul\OneDrive\Desktop\QIS\python\new.txt",mode = "a+")
# content = file.write("\nHello")
# file.seek(0)
# print(file.read())
# file.close()

# file = open(r"C:\Users\gokul\OneDrive\Pictures\Screenshots\Screenshot 2026-08-04 222305.png","rb")
# print(file.read())

# file = open(r"C:\Users\gokul\OneDrive\Documents\NNewResume.pdf","rb")
# print(file.read())

'''tell()'''
# file = open(r"C:\Users\gokul\OneDrive\Desktop\QIS\python\new.txt", "+a")
# file.seek(0)
# print(file.read())
# file.write("\nI am fine")
# print(file.tell())
# file.seek(5)
# print(file.read())

'''Context management'''
# with open(r"C:\Users\gokul\OneDrive\Desktop\QIS\python\new.txt",mode = "r") as file:
#     print(file.read())

'''reading csv'''
# import csv
# with open(r"C:\Users\gokul\Downloads\global_power_plant_database.csv","r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)

'''csv.DictReader'''
# import csv
# with open(r"C:\Users\gokul\OneDrive\Desktop\QIS\python\data.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row)

# print(row["Name"])
# print(row["Salary"])

'''Writing CSV file'''
import csv

data = [["Name", "Age", "Salary"],["Rahul", 26, 20000],["Anu",29,22000]]

with open("employee.csv", "w",newline="") as file:
    writer = csv.writer(file)

    writer.writerows(data)

'''os'''
'''file exists'''
# import os
# if os.path.exists("data.txt"):
#     print("File exist")
# else:
#     print("File doesnot exist")

'''is file'''
# import os
# if os.path.isfile("data.txt"):
#     print("It is a file")
# else:
#     print("Not a file")

'''it is a directory'''
# import os
# if os.path.isdir("data"):
#     print("Is directory")
# else:
#     print("Not a directory")

'''make directory'''
# import os
# os.mkdir("Report")

'''create nested directory'''
# os.makedirs(data/2012/report)

'''list files in directory'''
# files = os.listdir()
# print(files)

'''Delete a file'''
# os.remove("files.txt")

'''Remove an empty directory'''
# os.rmdir("reports")

'''Rename a file'''
# os.rename("old.txt", "new.txt")

'''Working with File Paths'''
# import os
# file = "2016.txt"
# folder = "report"

# path = os.path.join(folder,file)
# print(path)

'''Batch file processing'''
'''report/
sale_jan.txt
sale.feb.txt
...
sales.dec.txt'''

# import os

# folder = "report"

# for filename in os.listdir(folder):
#     path = os.path.join(folder, filename)
#     with open(path, "r") as file:
#         content = file.read()

#         print(filename)
#         print(content)

'''Practical Data Science Mini Use Case'''
'''1. Count the number of records in a file'''

# count = 0
# with open("customers.txt", "r") as file:
#     for line in file:
#         count += 1

# print("number of customers : ", count)

'''2. Count Errors in Log File'''
'''INFO User logged in
INFO Data loaded
ERROR Database connection failed
INFO Retry started
ERROR File not found
INFO Process completed'''

# error_count = 0

# with open("application.log", "r") as file:
#     for line in file:
#         if "ERROR" in line:
#             error_count += 1

# print("Number of error : ", error_count)

'''3. Calculate Average from File'''
'''marks.txt contains:

80
90
75
85
70'''

total = 0
mark = 0

# with open("marks.txt", "r") as file:
#     for line in file:
#         marks = float(line.strip())

#         total += marks
#         count += 1

# average = total / count
# print("Average marks is ", average)