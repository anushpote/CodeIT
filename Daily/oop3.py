# Special/Dunder/Magic Methods

# int, float, str
# matrix

# [1,2] [3,4]

# class Matrix:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __str__(self):
#         matrix_str_format = f"""
#         |   {self.a}    |
#         |   {self.b}    |
#         """
#         return matrix_str_format
    
#     def __add__(self, other):
#         if not isinstance(other, Matrix):
#             raise Exception("Second operand must be a matrix!")
#         new_a = self.a + other.a
#         new_b = self.b + other.b

#         new_martix = Matrix(new_a, new_b)
#         return new_martix
    
#     def __sub__(self, other):
#         if not isinstance(other, Matrix):
#             raise Exception("Second operand must be a matrix!")
#         return Matrix(self.a - other.a, self.b - other.b)
    
#     def __mul__(self, other):
#         return Matrix(self.a * other.a, self.b * other.b)

# a1 = Matrix(1, 2)
# a2 = Matrix(4, 3)

# # print(a1 + a2)
# # print(a1-a2)

# print(a1 * a2)

################################################

# Inheritance

class User:
    def __init__(self, username, password, email = "example@ex.com"):
        self.username = username

        if len(password) <6:
            raise Exception("Password must be 6 characters long")
        self.password = password

    def __str__(self):
        return f"{self.username}'s account"
    
# u1 = User("ram", "ram123@")

# print(u1)

class Student(User):    # class Student is inheriting from class User
    def __init__(self, username, password, father_name, email="optional.com"):  # Method overriding
        super().__init__(username, password, email)  
        self.father_name = father_name

s1 = Student("Ram","ram123@", "ram's father")

print(s1)