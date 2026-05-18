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

# Ctrl + I Windsurf Command

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

if english_passed:
    print("They passed")
else:
    print("They failed")

