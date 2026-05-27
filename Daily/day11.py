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

marks = ['45','36','50','76']

# For example

int_marks = [int(mark) for mark in marks]  # list comprehension
print(marks)
print(int_marks)

total = sum(int_marks)

print(total)
