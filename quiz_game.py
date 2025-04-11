print("Welcome To Quiz Game!!!")
question=input("Do you want to play? ")
if question.lower() != "yes":
    quit()
print("Start the game!")
score=0
bit=input("Who is the father of computers? ")
if bit.lower() == "charles babbage":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
bit=input("The term computer is derived from: ")
if bit.lower() == "latin":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
bit=input("First generation computers are made of: ")
if bit.lower() == "vaccum tubes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
bit=input("What is the fullform of CPU? ")
if bit.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
bit=input("Expand RAM? ")
if bit.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
bit=input("Expand ROM? ")
if bit.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
bit=input("GUI stands for: ")
if bit.lower() == "graphical user interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
bit=input("ALU stands for: ")
if bit.lower() == "arithmatic logic unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
bit=input("What is a process of searching bugs in software? ")
if bit.lower() == "debugging":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
bit=input("Who is the Inventor of WWW? ")
if bit.lower() == "tim berners lee":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("Congratulations!")
print("Your score is: ",score)
