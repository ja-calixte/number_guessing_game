import random

lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)

guesses = 0
guesses_easy = 10
guesses_medium = 5
guesses_hard = 3
guesses_extreme = 1

is_running = True

def easy():
    guesses = 1
    is_running = True

    print("\n----- EASY DIFFICULTY -----")
    print("Great! You have selected the Easy difficulty level.")
    print(f"You have {guesses_easy} chances to guess the number. Goodluck!")
    print(f"\nSelect a number between {lowest_number} and {highest_number}: ")

    while is_running:
        guess = input("Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)

            if guess < lowest_number or guess > highest_number:
                print("Invalid guess. Out of range.")

            elif not guesses == guesses_easy:

                guesses += 1
                if guess < answer:
                    print("Too low! Try again!")
                elif guess > answer:
                    print("Too high! Try again")
                elif guess == answer:
                    print("\n----- CONGRATULATIONS -----")
                    print("YOU GOT THE CORRECT ANSWER!")
                    print(f"Number of guesses: {guesses}")
                    is_running = False
                else:
                    print("Invalid Answer. Please try again.")

            else:
                print("\n----- GAME OVER -----")
                print("YOU LOST! BETTER LUCK NEXT TIME!")
                print(f"The correct answer was {answer}")
                print(f"Number of guesses: {guesses}")
                is_running = False

        else:
            print("Invalid Answer. Please try again.")

    try_again()

def medium():
    guesses = 1
    is_running = True

    print("\n----- MEDIUM DIFFICULTY -----")
    print("Great! You have selected the Medium difficulty level.")
    print(f"You have {guesses_medium} chances to guess the number. Goodluck!")
    print(f"\nSelect a number between {lowest_number} and {highest_number}: ")

    while is_running:
        guess = input("Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)

            if guess < lowest_number or guess > highest_number:
                print("Invalid guess. Out of range.")

            elif not guesses == guesses_medium:

                guesses += 1
                if guess < answer:
                    print("Too low! Try again!")
                elif guess > answer:
                    print("Too high! Try again")
                elif guess == answer:
                    print("\n----- CONGRATULATIONS -----")
                    print("YOU GOT THE CORRECT ANSWER!")
                    print(f"Number of guesses: {guesses}")
                    is_running = False
                else:
                    print("Invalid Answer. Please try again.")

            else:
                print("\n----- GAME OVER -----")
                print("YOU LOST! BETTER LUCK NEXT TIME!")
                print(f"The correct answer was {answer}")
                print(f"Number of guesses: {guesses}")
                is_running = False

        else:
            print("Invalid Answer. Please try again.")

    try_again()

def hard():
    guesses = 1
    is_running = True

    print("\n----- HARD DIFFICULTY -----")
    print("Great! You have selected the Hard difficulty level.")
    print(f"You have {guesses_hard} chances to guess the number. Goodluck!")
    print(f"\nSelect a number between {lowest_number} and {highest_number}: ")

    while is_running:
        guess = input("Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)

            if guess < lowest_number or guess > highest_number:
                print("Invalid guess. Out of range.")

            elif not guesses == guesses_hard:

                guesses += 1
                if guess < answer:
                    print("Too low! Try again!")
                elif guess > answer:
                    print("Too high! Try again")
                elif guess == answer:
                    print("\n----- CONGRATULATIONS -----")
                    print("YOU GOT THE CORRECT ANSWER!")
                    print(f"Number of guesses: {guesses}")
                    is_running = False
                else:
                    print("Invalid Answer. Please try again.")

            else:
                print("\n----- GAME OVER -----")
                print("YOU LOST! BETTER LUCK NEXT TIME!")
                print(f"The correct answer was {answer}")
                print(f"Number of guesses: {guesses}")
                is_running = False

        else:
            print("Invalid Answer. Please try again.")

    try_again()

def extreme():
    guesses = 1
    is_running = True

    print("\n----- EXTREME DIFFICULTY -----")
    print("Great! You have selected the Extreme difficulty level.")
    print(f"You have {guesses_extreme} chance to guess the number. Goodluck!")
    print(f"\nSelect a number between {lowest_number} and {highest_number}: ")

    while is_running:
        guess = input("Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)

            if guess < lowest_number or guess > highest_number:
                print("Invalid guess. Out of range.")

            elif not guesses == guesses_extreme:

                guesses += 1
                if guess < answer:
                    print("Too low! Try again!")
                elif guess > answer:
                    print("Too high! Try again")
                elif guess == answer:
                    print("\n----- CONGRATULATIONS -----")
                    print("YOU GOT THE CORRECT ANSWER!")
                    print(f"Number of guesses: {guesses}")
                    is_running = False
                else:
                    print("Invalid Answer. Please try again.")

            else:
                print("\n----- GAME OVER -----")
                print("YOU LOST! BETTER LUCK NEXT TIME!")
                print(f"The correct answer was {answer}")
                print(f"Number of guesses: {guesses}")
                is_running = False

        else:
            print("Invalid Answer. Please try again.")

    try_again()

def try_again():
    print("\n----- TRY AGAIN -----")
    start = input("Would you like to start again? (y/n): ").lower()
    if start == "y":
        main()
    elif start == "n":
        print("\n----- THANK YOU -----")
        print("Thank you for playing our game!")
        exit()

def main():
    print("\n----- DIFFICULTY -----")
    print("1. Easy (10 Guesses)")
    print("2. Medium (5 Guesses)")
    print("3. Hard (3 Guesses)")
    print("4. Extreme (1 Guess)")

    while True:
        difficulty_choice = input("What difficulty do you want? (1-4): ")
        if difficulty_choice == "1":
            easy()
        elif difficulty_choice == "2":
            medium()
        elif difficulty_choice == "3":
            hard()
        elif difficulty_choice == "4":
            extreme()
        else:
            print("Invalid Action. Please try again.")
            continue

if __name__ == "__main__":
    print("----- WELCOME TO NUMBER GUESSING GAME -----")
    print(f"I will be thinking of a number between {lowest_number} and {highest_number}!")
    while True:
        start = input("\nWould you like to start the game? (y/n): ").lower()
        if start == "y":
            main()
        elif start == "n":
            print("\n----- THANK YOU -----")
            print("Thank you for playing our game!")
            exit()
        else:
            print("Invalid Action. Please try again.")
            continue




