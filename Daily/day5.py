# Data Structures

# 1. List

# list_of_numbers = [1, 2, 3, 4]

# mixed_list = [1, "Ram", 5.5, "Kathmandu", True]

#participants = []

#print(type(participants))

# participants.append("Sita")  #['Ram']
# participants.append("Rita") #['Ram', 'Hari']
# participants.append("Ram")
# participants.append("Hari")
#participants.append("Shyam")

#participants.insert(0, "Shyam")

# print("Index of Ram is: ", participants.index("Ram"))
# print("Index of Shyam is: ", participants.index("Shyam"))
# print("Index of Hari is: ", participants.index("Hari"))

#print(participants)

#participants.remove("Sita") # Removes if exists, If it doesn't exist, it gives error saying it isn't on the list

# participants.pop()

# print(participants)

######################################################

participants = ["ram", "hari", "shyam"]

#print(participants)

# for name in enumerate(participants, start=5):   # enumerate(start from 5, for e.g.: (5, 'ram') )
#     print(name)

# for num, name in enumerate(participants, start=1):
#     print(num, name)

######################################################

#while True:
#     new_name = input("Enter new participant's name: (Enter 'q' to quit)")
#     if new_name == "q":
#         break
#     participants.append(new_name)

# for num, name in enumerate(participants, start=1):
#     print("List of participants: ", participants)

# participants = []

# MENU = """
#     ============MENU==========
#     1. Add new participant
#     2. Remove existing participant
#     3. Show all participants
#     Q. Quit

# """

# while True:
#     choice = input("Enter your choice (1, 2, 3, Q/q): ").upper()
#     if choice == "Q":
#         print("Thank you for using our program!")
#         break
#     elif choice == "1":
#         new_name = input("Enter new participant's name: ")
#         participants.append(new_name)
#         print(f"Added new participant {new_name}")
#     elif choice == "2":
#         print(f"The list of participants are: {participants}")
#     elif choice == "3":
#         remove_name = input("Enter the name you want to remove: ")
#         if remove_name in participants:
#             participants.remove(remove_name)
#             print(f"{remove_name} has been removed from the list!")
#     else:
#         print("Please enter right choice!")
#     print(MENU)
    

# Tuple
final_participants = tuple(participants)

#print("final", final_participants)

# ['ram', 'hari'] -> list can be modified, mutable
# ('ram', 'hari') -> tuple cannot be modified once created, immutable

tuple_example = ("ram", "hari", "sita", "gita")

#tuple_example.append() -> cannot append, inserted or modified

num, name = 1, "Ram"    #unpacking

# for data in enumerate(participants, start=1):
#     print(data)

a, *mids, b = 1, 2, 3, 4

print(a)
print(mids)
print(b)