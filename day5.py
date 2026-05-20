# Data Structures

# 1. List

# list_of_numbers = [1, 2, 3, 4]

# mixed_list = [1, "Ram", 5.5, "Kathmandu", True]

participants = []

#print(type(participants))

participants.append("Ram")  #['Ram']
participants.append("Hari") #['Ram', 'Hari']

participants.insert(0, "Shyam")

print("Index of Ram is: ", participants.index("Ram"))
print("Index of Shyam is: ", participants.index("Shyam"))
print("Index of Hari is: ", participants.index("Hari"))

print(participants)