import random
while True:
    user_action = input("Enter a choice. Rock/Paper/Scissors")
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    print(f"You choose{user_action},Computer choice{computer_action}")