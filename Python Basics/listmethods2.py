numbers = [ 10,20 , 25 , 40 , 50 ,50]
for item in numbers:
    if numbers.count(item)>1:
        numbers.remove(item)
print(numbers)