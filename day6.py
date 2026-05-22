numbers = [1,20,5,6,100, -3, 43]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers[1:]: # numbers[1:] slicing
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest:
        second_largest = num

print("Largest Number: ", largest)
print("Second Largest: ", second_largest)