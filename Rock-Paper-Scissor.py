import random

def get_computer_choice():
    """Randomly select a choice for the computer."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    """Determine the winner of the game."""
    if player_choice == computer_choice:
        return "It's a tie!"
    
    if (player_choice == "rock" and computer_choice == "scissors") or \
       (player_choice == "scissors" and computer_choice == "paper") or \
       (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    
    return "You lose!"

def play_game():
    """Play a game of Rock-Paper-Scissors."""
    print("Welcome to Rock-Paper-Scissors!")
    
    choices = ["rock", "paper", "scissors"]
    
    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        
        if player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
if __name__ == "__main__":
    play_game()
