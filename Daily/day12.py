# Lambda function (anonymous function) / (anon function) Used for a single use

# def cube(x):
#     return x**3

#cube = lambda x:x**3

# Higher order function like map and filter

# len, int, str

# marks = ['45','36','50','76']

# int_marks = tuple(map(int, marks))
# int_marks = list(map(int, marks))

# print(int_marks)

# int_marks = map(int, marks)

# for mark in int_marks:
#     print(mark)

# print(next(int_marks))  # lazy evaluation
# print(next(int_marks))  # lazy evaluation

marks = ['45','26','50','76']

int_marks = list(map(int, marks))

print(int_marks)

# def pass_fail(mark):
#     if mark >= 30:
#         return 'P'
#     else:
#         return 'F'

marks_to_pass_fail = map(lambda mark:'P' if mark >= 30 else 'F', int_marks)

print(list(marks_to_pass_fail))