import random
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    choices = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        print("\nChoose an option: 1. Rock, 2. Paper, 3. Scissors. Type '0' to quit.")
        try:
            user_input = int(input("Your choice (1-3): "))
            if user_input == 0:
                print("\nThanks for playing!")
                print(f"Final Scores: You: {user_score}, Computer: {computer_score}")
                break
            if user_input not in [1, 2, 3]:
                print("Invalid choice. Please choose 1, 2, or 3.")
                continue
            user_choice = choices[user_input - 1]
            computer_choice = get_computer_choice()
            print(f"You chose: {user_choice}")
            print(f"Computer chose: {computer_choice}")
            winner = determine_winner(user_choice, computer_choice)
            if winner == "tie":
                print("It's a tie!")
            elif winner == "user":
                print("You win this round!")
                user_score += 1
            else:
                print("Computer wins this round!")
                computer_score += 1
            print(f"Scores: You: {user_score}, Computer: {computer_score}")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3, or 0 to quit.")
if __name__ == "__main__":
    play_game()