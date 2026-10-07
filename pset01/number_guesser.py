import random

while True:
    number = random.randint(1, 1000)
    attempts = 0

    while True:
        guess = input("Guess a number between 1 and 1000 (or type 'bye'/'exit'): ")

        if guess == "bye" or guess == "exit":
            print("Goodbye!")
            exit()

        if not guess.isdigit():
            print("Please enter a valid number")
            continue

        guess = int(guess)
        attempts += 1

        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("Congratulations! You guessed the number!")
            print("Attempts:", attempts)
            break
