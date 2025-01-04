import random

while True:  
    computer = random.choice([1, 0, -1])
    user = input("Enter your choice (Snake/Water/Gun): ")
    user = user.strip().upper()
    user_dict = {"SNAKE": 1, "WATER": 0, "GUN": -1}

    if(user not in user_dict):
        print("Invalid choice!!")
        continue

    user = user_dict[user]

    reverse_dict = {1: "SNAKE", 0: "WATER", -1: "GUN"}

    print(f"You chose: {reverse_dict[user]}")
    print(f"Computer chose: {reverse_dict[computer]}")

    if(user == computer):
        print("It's a tie!!")
    else:
        if(user == 1 and computer == 0):
            print("You win!!")
        elif(user == 1 and computer == -1):
            print("You lose!!")
        elif(user == 0 and computer == 1):
            print("You lose!!")
        elif(user == 0 and computer == -1):
            print("You win!!")
        elif(user == -1 and computer == 1):
            print("You win!!")
        elif(user == -1 and computer == 0):
            print("You lose!!")
        else:
            print("Something went wrong!!")
        
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if(play_again != "yes"):
            break

print("Thanks for playing!!")