# Exception Handling

#1a = 5  # Syntax error. Not exception

try:
    user_input = int(input("Enter a number: "))
except ValueError:
    print("Please enter numeric value only. For example: 123")
except Exception as e2:
    print("Something went wrong!", e2)

print("Something running")

print("Program ends here")