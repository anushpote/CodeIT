# # 1. Reading a Text File
# with open("mytext.txt", "r") as file:
#     content = file.read()

# print(content)

###############################################

# 1. Reading a Text File line by line
# with open("mytext.txt", "r") as file:
#     #content = file.read()
#     for line in file.readlines():
#         print(line)

###############################################

# WPA/WPS Tester

# #admin123 -> 3424fsjd09iwe
# wifi_password = "admin123"  # Pretend the password is encoded
# with open("mytext.txt","r") as passwords_file:
#     print(type(passwords_file))
#     for password in passwords_file:
#         cleaned_pass = password.strip() # strip(): remove the new line that spawns when you press enter
#         #print(cleaned_pass, len(cleaned_pass)) # not necessary to print this line
#         #hash_value = calculate_hash(cleaned_pass) -> 3424fsjd09iwe

#         # if hash_value == wifi_password:
#         #     print("Password Found", cleaned_pass)

#         if cleaned_pass == wifi_password:
#             print("Password Found", cleaned_pass)

######################################################
# Writing in a file (Guess number game)
# import random

# # Generate random number between 1 to 100

# secret_number = random.randint(1, 100)

# print("Welcome to the Number Guessing Game!")

# print("Guess a number between 1 and 100")

# with open("guess_game_counter.txt", "r") as file:
#     current_min_guess = file.read()

# if current_min_guess.strip() == "0":
#     print("No one has scored")
# else:
#     print("Minimum guesses till now: ", current_min_guess)

# print("Minimum guess till now: ", )

# counter = 0

# while True:
#     guess = int(input("Enter your guess: "))

#     counter += 1
#     if guess < secret_number:
#         print("Too low")
#     elif guess > secret_number:
#         print("Too high")
#     else:
#         print("Congratulation! You guessed the correct number")
#         break

# print("You made successful guess after ", counter, "times")
# print("Minimum guess till now: ", current_min_guess)

# if int(current_min_guess) == 0 or counter < int(current_min_guess):
#     with open("mytext.txt","w") as file:
#         file.write(str(counter))

#####################################################

#   Writing in a file and Append in a file

# with open("web_logs.txt","a") as file:
#     user_inputs =[]
#     while True:
#         user_input = input("(q for quit)>>> ").lower()
#         if user_input == "q":
#             break
#         user_inputs.append(f"{user_input}\n")

#     file.writelines(user_inputs)

#######################################################

# CSV Module

import csv

with open("class6marks.csv","r") as file:
    #reader = csv.reader(file, delimiter="|")    # if there is no comma in the list. Delimeter can be used to mark a symbol as a separator. Here | is now a separator

    reader = csv.reader(file)
    header = next(reader)   # reader will return first row
    for row in reader:
        #print(row)
        name = row[0]
        marks = row[1:]

        print("Student ", name)
        print("Marks: ", marks)

        total = 0
        no_of_sub = len(marks)
        for mark in marks:
            int_mark = int(mark)
            total += int_mark
        percentage = total/no_of_sub
        print(name, percentage, "%")