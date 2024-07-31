#Emoji Converter

message = input('>')

words = message.split(' ')

emojis = {
    ":)": "Smiley Emoji",
    ":(": "Sad Emoji"
}

output = ""

for word in words:
    output += emojis.get(word, word) + " "
print(output)