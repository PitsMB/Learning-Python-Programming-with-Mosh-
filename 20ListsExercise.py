numbers = [50, 10, 20 ,30, 40, 30, 30, 10, 10]

for number in numbers:
   if numbers.count(number) > 1:
      numbers.remove(number)
numbers.sort()
print(numbers)
