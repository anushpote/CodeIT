# Exception Handling

#1a = 5  # Syntax error. Not exception

while True:
    try:
        user_input = int(input("Enter a number: "))
    except ValueError:  # if user enter wrong value
        print("Please enter numeric value only. For example: 123")
    except Exception as e2:
        print("Something went wrong!", e2)
    else:
        break

print("Something running")

print("Program ends here")