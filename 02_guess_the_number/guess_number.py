import random

print("🎯 Welcome to Guess the Number Game!")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter a number between 1 and 100: "))
        attempts += 1

        if guess < secret_number:
            print("📉 Too Low! Try Again.")

        elif guess > secret_number:
            print("📈 Too High! Try Again.")

        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("❌ Please enter a valid number.")