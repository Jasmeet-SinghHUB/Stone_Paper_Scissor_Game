from game.utils import get_user_choice, get_computer_choice
from game.logic import decide_winner

def play_game():
    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        
        result = decide_winner(user, computer)
        print("Result:", result)
        
        if input("Play again? (y/n): ").lower() != 'y':
            break
while True:
    print("\n1. Play Game\n2. Exit")
    choice = int(input("Enter option: "))
    
    if choice == 1:
        play_game()
    elif choice == 2:
        print("Goodbye!")
        break
    else:
        print("Invalid option!")