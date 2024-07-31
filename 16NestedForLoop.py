#Nested loops
numbers = [2, 2, 2, 2, 7]

for x in numbers:
    result = ''
    for y in range(x):
        result += 'x'
    print(result)