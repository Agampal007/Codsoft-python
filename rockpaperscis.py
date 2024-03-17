import random

def get_user_choice():
    print("Choose your weapon:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    winning_combinations = [(1, 3), (3, 2), (2, 1)]
    if (user_choice, computer_choice) in winning_combinations:
        return "You win!"
    else:
        return "Computer wins!"

def print_choices(choice, player):
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"{player} chose {choices[choice]}")

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print_choices(user_choice, "You")
    print_choices(computer_choice, "Computer")

    result = determine_winner(user_choice, computer_choice)
    print(result)

while True:
    play_game()

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing. Goodbye!")
        break
