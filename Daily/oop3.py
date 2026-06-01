# Special/Dunder/Magic Methods

# int, float, str
# matrix

# [1,2] [3,4]

class Matrix:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        matrix_str_format = f"""
        |   {self.a}    |
        |   {self.b}    |
        """
        return matrix_str_format
    
    def __add__(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b

        new_martix = Matrix(new_a, new_b)
        return new_martix


a1 = Matrix(1, 2)
a2 = Matrix(4, 3)

print(a1 + a2)