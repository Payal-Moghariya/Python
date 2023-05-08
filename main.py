import random


def get_choices():
    player_choice = input("Enter a choice : Rock/Paper/Scissors : ")
    
    random_choice = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(random_choice)

    choices = { "player":player_choice, "computer": computer_choice }
    return choices

def check_win(player, computer):
    print(f"You chose : {player}  , Computer choice : {computer} ")
    
    if(player == computer):
        return "Its a tie!"
    
    elif player == "Rock":
        if computer == "Scissors":
            return "You Win"
        else:
            return "You lose"
        
    elif player == "Paper":
        if computer == "Rock":
            return "You Win"
        else:
            return "You lose"
    elif player == "Scissors":
        if computer == "Paper":
            return "You Win"
        else:
            return "You lose"
        

choices = get_choices()

resolved = check_win(choices["player"],choices["computer"])
print(resolved)



        
    


    


