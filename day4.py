# Control flow
# #Conditional Statements

# #Looping Statements
# 1. Finite Loop (for _ in )

# for i in range(1, 5, 2):    # 1 is starting value, 5 is stopping value, 5 is excluded, 2 is called step value
#     print("Welcome home", i)


# Multiplication Table
# Table of 2

# for num in range(1, 11,):
#     print(f"3 * {num} = {num*3}")

# Multiplication of any number

# number = int(input("Enter any number for multiplication table: "))

# for num in range(1, 11):
#     print(f"{number} * {num} = {number*num}")

# for and for each loop
# sentence = "We love Nepal"
# vowels = "aeiouAEIOU" 
# count = 0

# for each_char in sentence:
#     #check if its a vowel
#     if each_char in vowels:
#         count += 1
#         print(each_char)
        
#     elif each_char==" ":
#         print("Here is space")
#     else:
#         print(f"{each_char} is a consonant")

# print(f"There are {count} vowels")

#2 Infinite Looping (while loop)

batti_cha = True

while batti_cha:
    print("Fan ghumdai xa")

    user_answer = input("Batti xa? (yes/no)")

    if user_answer == "yes":
        batti_cha = True
    elif user_answer == "no":
        batti_cha = False
    else:
        print("Write only yes or no!!!")
