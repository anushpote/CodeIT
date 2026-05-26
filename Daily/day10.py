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

wifi_password = "admin123"  # Pretend the password is encoded
with open("mytext.txt","r") as passwords_file:
    for password in passwords_file:
        cleaned_pass = password.strip() # strip(): remove the new line that spawns when you press enter
        #print(cleaned_pass, len(cleaned_pass)) # not necessary to print this line

        if cleaned_pass == wifi_password:
            print("Password Found", cleaned_pass)