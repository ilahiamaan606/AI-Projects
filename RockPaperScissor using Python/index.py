import random

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter your choice (rock, paper, or scissors), or 'quit' to exit: ")

    if user_choice.lower() == "quit":
        break

    computer_choice = random.choice(choices)

    if user_choice.lower() == computer_choice:
        print("It's a tie!")
    elif user_choice.lower() == "rock":
        if computer_choice == "scissors":
            print("You win! Rock beats scissors.")
        else:
            print("You lose! Paper beats rock.")
    elif user_choice.lower() == "paper":
        if computer_choice == "rock":
            print("You win! Paper beats rock.")
        else:
            print("You lose! Scissors beats paper.")
    elif user_choice.lower() == "scissors":
        if computer_choice == "paper":
            print("You win! Scissors beats paper.")
        else:
            print("You lose! Rock beats scissors.")
    else:
        print("Invalid choice. Please enter one of the following: rock, paper, or scissors.")

print("Thank you for playing!")
