# Function
# Function is a block code that represents a specific task
# Function is a variable that store group of code

# def welcome_message():  #Function Definition
#     print("Welcome Ram")
#     print("Please check your email and verify your account")

# welcome_message # Function call

# print(welcome_message())

# If a paremeter has a default value, its called a defaul paramenter
def welcome_message(name, greeting="Welcome"):  # Only return "Welcome" in greeting if greeting is not given as argument/ empty
    print(greeting, name)
    print("Please check your email and verify your account")

# Actual data sent for a parameter, for e.g. "Ram is called as argument. But in general it can simply be called as para/meter"
welcome_message("Ram", "Good Morning") # Returns -> Good Morning Ram
welcome_message("Ram") # Return -> Welcome Ram
