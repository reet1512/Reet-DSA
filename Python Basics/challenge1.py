word = input("Enter a word: ")
letters = list(word)
counter =0
for items in letters:
    if items == "a" or items == "e" or items == "i" or items == "o" or items == "u":
         counter +=1
print(counter)