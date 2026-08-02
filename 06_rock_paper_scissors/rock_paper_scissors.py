import random

choices = ["rock", "paper", "scissors"]

print("=== Rock Paper Scissors ===")

while True:
    user = input("\nEnter Rock, Paper or Scissors: ").lower()

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("You:", user)
    print("Computer:", computer)

    if user == computer:
        print("It's a Tie!")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You Win!")

    else:
        print("Computer Wins!")

    again = input("\nPlay Again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break