a= 5
b= 10

#Arithemetic Operators
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b) #Integer division quotient
# print(a%b) #modulo -> Remainder
# print(a**b) #power

#Relational Operators
# print(5>2)
# print(5<2)
# print(5>=2)
# print(5<=2)
# print(5==2)
# print(5!=2)

#Logical Operators (and, or, not)
print(5>2 and 5>3 and 5<10)

print(5>2 and 5>3 and 5>10)

print(5>2 or 5<10)

print(5>2 or 5>10)

print(not 5<2)

#1st example (Find it a student has passed and exam)

english_marks = int(input("Enter marks of english"))
english_pass_marks = 30

english_passed = english_marks>=english_pass_marks

#The gap before print in line 43 and 45 is called Indentation
if english_passed:
    print("They passed")
else:
    print("They failed")

#2nd example
if english_marks >= 90:
    print("A+")
elif english_marks >= 80:
    print("A")
elif english_marks >= 70:
    print("B+")
else:
    print("B")