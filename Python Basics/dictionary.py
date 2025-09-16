
numbers = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
inputs = input("Enter multiple values: ")
length = ""
for  items in inputs:
  length += numbers.get(items+"")
print(length)
