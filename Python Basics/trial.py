def emojiconverter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😞"
    }
    output = ""
    for word in words:
        # The get() method looks for the word in the dictionary.
        # If it's not found, it returns the word itself.
        output += emojis.get(word, word) + " " # Added a space for readability
    return output # This should be outside the for loop


message = input(">")
print(emojiconverter(message))