#Lists
numbers = [1, 2, 3, 4, 5]
highest = numbers[0]
for number in numbers:
    if number > highest:
        highest = number
print(highest)