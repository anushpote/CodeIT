# 1. Reading a Text File
with open("mytext.txt", "r") as file:
    content = file.read()

print(content)