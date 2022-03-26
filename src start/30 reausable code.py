# write emoji function (25)

def emoji_converter(massage):
    words = massage.split(' ')


    emojis = {
        "(:": "😊",
        ":(": "☹"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


massage = input(">")
print(emoji_converter(massage))
