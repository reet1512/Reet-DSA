secretnumber = 10
guesscount = 0
guesslimit = 3
while guesscount < guesslimit:
   guess = int(input("Guess"))
   guesscount +=  1 
   if guess  ==  secretnumber:
        print("You won")
        break
else:
    print("Sorry you failed")