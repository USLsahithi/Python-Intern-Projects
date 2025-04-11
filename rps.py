import random
user_winning=0
computer_winning=0
choices=["rock","paper","scissors"]
while True:
    user_choice=input("Enter your choice: Rock/Paper/Scissors/Q to quit ").lower()
    if user_choice=='q':
        break
    if user_choice not in choices:
        continue
    number_choosen=random.randint(0,2)
    computer_choice=choices[number_choosen]
    print("Computer choice: ",computer_choice+".")
    if user_choice=="rock" and computer_choice=="scissors":
        print("Won!")
        user_winning+=1
    elif user_choice=="paper" and computer_choice=="rock":
        print("Won!")
        user_winning+=1
    elif user_choice=="scissors" and computer_choice=="paper":
        print("Won!")
        user_winning+=1
    elif user_choice==computer_choice:
        print("Tie!")
        continue
    else:
        print("Lost!")
        computer_winning+=1
print("You won: ",user_winning,"times.")
print("Computer won: ",computer_winning,"times.")
        
