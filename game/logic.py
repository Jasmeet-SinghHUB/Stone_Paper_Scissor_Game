def decide_winner(user, computer):
    print(f"\nYou: {user} | Computer: {computer}")
    
    if user == computer:
        return "Draw"
    
    elif (user == "Stone" and computer == "Scissors") or \
         (user == "Paper" and computer == "Stone") or \
         (user == "Scissors" and computer == "Paper"):
        return "You Win 🎉"
    
    else:
        return "Computer Wins 🤖"