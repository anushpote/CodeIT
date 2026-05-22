# Function
# Function is a block code that represents a specific task
# Function is a variable that store group of code

# def welcome_message():  #Function Definition
#     print("Welcome Ram")
#     print("Please check your email and verify your account")

# welcome_message # Function call

# print(welcome_message())

#############################################################################

# If a paremeter has a default value, its called a defaul paramenter

# def welcome_message(name, greeting="Welcome"):  # Only return "Welcome" in greeting if greeting is not given as argument/ empty
#     print(greeting, name)
#     print("Please check your email and verify your account")

######################################################################

# Actual data sent for a parameter, for e.g. "Ram is called as argument. But in general it can simply be called as para/meter"
# welcome_message("Ram", "Good Morning") # Returns -> Good Morning Ram
# welcome_message("Ram") # Return -> Welcome Ram
#welcome_message(name="Ram", greeting="Hello")   # This usage is called as keyword argument

#################################################################

# WRONG / CANNOT RUN / ERROR
# def welcome_message(greeting="Welcome", name):  # Cannot put default parameter in first, always in last
#     print(greeting, name)
#     print("Please check your email and verify your account")

#############################################################

def add(a,b):
    print(a+b)

    return a+b  # if return is not written, it prints "None"

result = add(3,4)

print("result", result)