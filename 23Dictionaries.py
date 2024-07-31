#Dictionary
numbers = input('Phone: ')

digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = ""

for number in numbers:
    output += digits.get(number, "!") + " "
print(output)