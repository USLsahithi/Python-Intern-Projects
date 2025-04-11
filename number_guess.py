import random
number=input("Enter a number: ")
if number.isdigit():
    number=int(number)
    if number<=0:
        print("Enter a number greater than 0")
        quit()
else:
    print("Enter numbers only!!")
    quit()
random_number=random.randint(0,number)
guesses=0
while True:
    guesses+=1
    guess_no=input("Guess the number: ")
    if guess_no.isdigit():
        guess_no=int(guess_no)
    else:
        print("Enter numbers only!!")
        continue
    if guess_no==random_number:
        print("Correct!")
        break
    else:
        print("Wrong!")
print("You guessed the number in",guesses,"guesses")
