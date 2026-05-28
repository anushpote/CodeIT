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

# marks = ['100','45','26','50','76']

# int_marks = list(map(int, marks))

# print(int_marks)

# # def pass_fail(mark):
# #     if mark >= 30:
# #         return 'P'
# #     else:
# #         return 'F'

# marks_to_pass_fail = map(lambda mark:'P' if mark >= 30 else 'F', int_marks)

# print(list(marks_to_pass_fail))

# int_marks.sort()

# print(int_marks)

# sorted_marks = sorted(int_marks)  #Ascending

# sorted_marks = sorted(int_marks, reverse=True)  #Descending

# print(sorted_marks)

# stu_marks = {
#     "ram": 89,
#     "hari": 78,
#     "sita": 49,
#     "gita": 100
# }

# def return_value(item):
#     return item[1]

# sorted_marks = sorted(stu_marks.items())
# sorted_marks = sorted(stu_marks.items(), key= return_value)
# sorted_marks = sorted(stu_marks.items(), key= lambda item:item[1], reverse=True)

# print(sorted_marks)

# ranked_stu_marks = dict(sorted_marks)

# print(ranked_stu_marks)

########################################################

# Iterator

# marks = ['100','45','26','50','76']

# # print(marks.__iter__)

# mi = iter(marks)

# print(next(mi))
# print(next(mi))
# print(next(mi))

# print(type(mi))

####################################

# marks = ['100','45','26','50','76']
# mi = iter(marks)
# print(next(mi))
# print(next(mi))
# print(next(mi))
# print(next(mi))
# print(next(mi))
# print(next(mi))

# while True:
#     try:
#         value = next(mi)
#     except StopIteration:
#         print("End of list")
#         break
#     else:
#         print(value)

# print("End of while loop")