a = 10
print(a)

a = 10
b = 11
print(a+b)

x="10"
y="20"
print(x+y)

a = 10
b = a
c = 10
print(a is b)
print(a is c)
print(c is b)

print(id(a))
print(id(b))
print(id(c))

a = 10
b = 10
print(id(a))
print(id(b))

a = "abcd"
b = "abcd"
c = a
print(id(a))
print(id(b))
print(a is b)
print(b is c)
print(id(c))

l1=[1,2,3,4]
l2=[1,2,3,4]
l3=l1
print(l1 is l2)
print(l1 is l3)
print(l2 is l3)

a=10000
b=10000
print(a is b)

student = {
    "name": "Anjali",
    "age": 25,
    "mark": 95
}
print(student)

