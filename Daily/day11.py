# Exception Handling

#1a = 5  # Syntax error. Not exception

#   VALUE ERROR
# while True:
#     try:
#         user_input = int(input("Enter a number: "))
#     except ValueError:  # if user enter wrong value
#         print("Please enter numeric value only. For example: 123")
#     except Exception as e2:
#         print("Something went wrong!", e2)
#     else:
#         break

# print("Something running")

# print("Program ends here")

##############################################################################

# Using finally

# students = ["ram","hari","shyam"]

# try:
#     students.remove("shyam")
# except ValueError:
#     print("The item you are trying to remove does not exist.")
# else:
#     print("Removed successfully")
# finally:
#     print("Student Removal program completed")

#####################################################

# FileNotFoundError 

# try:
#     with open("new.txt","r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("The file does not exist.")
#     print("Please check the file name or file path.")

#######################################################

# Comprehensions: (More effective operations similar to loop)

# marks = ['45','36','50','76']

# # For example

# int_marks = [int(mark) for mark in marks]  # list comprehension
# print(marks)
# print(int_marks)

# total = sum(int_marks)

# print(total)

#########################################################

# Even and odd using comprehension

# nums = [1,2,3,4,5,6,7,8,9,10]

# even_numbers = [num for num in nums if num % 2 == 0]
# odd_numbers = [num for num in nums if num % 2 != 0]

# # 1. what to keep in new list ?
# # 2. where does that come from ?
# # 3. (optional) on what condition new value should be kept ?

# print(even_numbers)
# print(odd_numbers)

####################################################################

# # Flipping items in list

# life_to_emotion = {
#     5: "🫡",
#     4: "😣",
#     3: "😢",
#     2: "😭",
#     1: "😅"
# }

# emotion_to_life = {
#     value:key
#     for key, value in life_to_emotion.items()
# }
# print(life_to_emotion)
# print(emotion_to_life)

#######################################################

# # Decorator: (decorates existing function)

# def deco(func):
#     def wrapper_func():
#         print("this is before function")
#         func()
#         print("this is after the function")

#     return wrapper_func

# @deco
# def just_func():
#     print("this is just a function")

# just_func()

################################################

# Use Case of Decorator

# # Measure execution time
# import time 

# start = time.time()
# # some task
# for i in range(1000000):
#     pass
# time.sleep

# end = time.time()

import time
 
def show_execution_time(func):
    def wrapper_func(*args, **kwargs):
        
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Execution time: ", end-start, "seconds")
    return wrapper_func

@show_execution_time
def heavy_task_func(a, b=0):    
    print("Heavy Task Start")
    time.sleep(3.5)
    print("Values are: ", a, b)
    print("Heavy Task End")

heavy_task_func(0,1)

# @show_execution_time
# def a(a,b,c):
#     pass