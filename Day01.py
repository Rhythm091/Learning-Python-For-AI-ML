import random

def get_choices():
    while True:
        player_choices = input("Enter a choice (rock, paper, scissors): ").lower()
        if player_choices in ["rock", "paper", "scissors"]:
            break
        print("Invalid choice! Please type rock, paper, or scissors.")

    options = ["rock", "paper", "scissors"]
    computer_choices = random.choice(options)
    choices = {"player": player_choices, "computer": computer_choices}
    return choices

player_Score = 0
computer_Score = 0

while True:
    choices = get_choices()
    print(f"You chose {choices['player']}, computer chose {choices['computer']}.")

    if choices["player"] == choices["computer"]:
        print("It's a tie!")
    elif choices["player"] == "rock" and choices["computer"] == "paper":
        print("Computer Wins this round!")
        computer_Score += 1
    elif choices["player"] == "paper" and choices["computer"] == "scissors":
        print("Computer Wins this round!")
        computer_Score += 1
    elif choices["player"] == "scissors" and choices["computer"] == "rock":
        print("Computer Wins this round!")
        computer_Score += 1
    else:
        print("Player Wins this round!")
        player_Score += 1

    print(f"Player score: {player_Score} | Computer score: {computer_Score}")

    if computer_Score == 3:
        print("\nComputer reached 3 points and won the match!")
        break

    if player_Score == 3:
        print("\nCongratulations! You reached 3 points and won the match!")
        break

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes" and play_again != "y":
        print("\nThanks for playing!")
        print(f"Final score -> Player: {player_Score} | Computer: {computer_Score}")
        break