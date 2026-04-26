import random

options = ["Stone", "Paper", "Scissors"]

def get_user_choice():
    print("\n1. Stone  2. Paper  3. Scissors")
    choice = int(input("Enter choice (1-3): "))
    
    if choice in [1, 2, 3]:
        return options[choice - 1]
    else:
        print("Invalid choice!")
        return get_user_choice()

def get_computer_choice():
    return random.choice(options)