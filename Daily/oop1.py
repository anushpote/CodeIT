# OOP (Object Oriented Programming)
# Object and Class

class Student:
    def __init__(self, name, address, marks):
        self.name = name
        self.address = address
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            print("A+")
        elif self.marks >= 80:
            print("A")
        elif self.marks >= 70:
            print("B+")
        else:
            print("B")

s1 = Student("ram","ktm",80)
s2 = Student("hari","bhkt",60)

s1.calculate_grade()
s2.calculate_grade()