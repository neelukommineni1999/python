# Practice 11: Find the largest number in the list
numbers = [32, 65, 23, 76, 54, 89, 12]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)
