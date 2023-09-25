import random

# List of possible actions
actions = ["Rock", "Paper", "Scissors"]

while True:
    # Computer's random choice
    computer_choice = random.choice(actions)

    # Player's input
    player_choice = input("Enter your choice (Rock/Paper/Scissors) or 'I quit' to exit: ").strip().capitalize()

    # Check if the player wants to quit
    if player_choice == "I quit":
        print("Thank you for playing!")
        break

    # Check if the player's choice is valid
    if player_choice not in actions:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        continue

    # Determine the winner
    if player_choice == computer_choice:
        print("Game Tied")
    elif (player_choice == "Rock" and computer_choice == "Paper") or \
         (player_choice == "Scissors" and computer_choice == "Rock") or \
         (player_choice == "Paper" and computer_choice == "Scissors"):
        print(f"You lose. Computer chose {computer_choice}.")
    else:
        print(f"You win! Computer chose {computer_choice}.")
