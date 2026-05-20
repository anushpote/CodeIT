# Excersise 1: Print Numbers from 1 to 10
# for _ in range(1,11):
#     print(_)

##################

#Exercise 2: Print Numbers from 10 to 1
# for _ in range(10, 0, -1):
#     print(_)

#####################

# Exercise 3: Multiplication Table

num = int(input("Enter a number to generate multiplication table upto 10: "))
for _ in range(1, 11):
    print(f"{num} * {_} = {num * _}")