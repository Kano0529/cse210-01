

slot = [1,2,3,4,5,6,7,8,9]

def main():

    print_game_board()
    winner_not_found = True
    counter = 1

    while winner_not_found and counter < 10:

        player = check_player(counter)

        choice = check_input(player)

        if player == 'x':
            slot[choice-1] = 'x'
        else:
            slot[choice-1] = 'o'
    
        print_game_board()

        winner_not_found = winner_is(player)
        if winner_not_found == False:
            print(f"{player} won!")

        counter += 1
   
    if winner_not_found == True:
        print(f"It's a draw. Nice game!")


def print_game_board():
    
    print(f"{slot[0]}|{slot[1]}|{slot[2]}")
    print(f"-+-+-")
    print(f"{slot[3]}|{slot[4]}|{slot[5]}")
    print(f"-+-+-")
    print(f"{slot[6]}|{slot[7]}|{slot[8]}")
    print()  


def check_input(player):
    
    choice = input(f"{player}'s turn to choose a square (1-9): ")
    while not(choice.isnumeric()) or (int(choice) not in slot):
        print("Please enter the valid number.")

        choice = input(f"{player}'s turn to choose a square (1-9): ")

    return int(choice)


def check_player(current_counter):
    
    turn_list = [1, 3, 5, 7, 9]
    
    # if the turn is odd number turn, it's x's turn. Otherwise it's O's turn.
    if current_counter in turn_list:
        player = 'x'
    else:
        player = 'o'
        
    return player           


def winner_is(player): 
    
    if (slot[0] == player) and (slot[1] == player) and (slot[2] == player):
        winner_not_found = False

    elif (slot[3] == player) and (slot[4] == player) and (slot[5] == player):
        winner_not_found = False

    elif (slot[6] == player) and (slot[7] == player) and (slot[8] == player):
        winner_not_found = False

    elif (slot[0] == player) and (slot[3] == player) and (slot[6] == player): 
        winner_not_found = False

    elif (slot[1] == player) and (slot[4] == player) and (slot[7] == player):
        winner_not_found = False

    elif (slot[2] == player) and (slot[5] == player) and (slot[8] == player):
        winner_not_found = False

    elif (slot[0] == player) and (slot[4] == player) and (slot[8] == player):
        winner_not_found = False

    elif (slot[2] == player) and (slot[4] == player) and (slot[6] == player):
        winner_not_found = False
    else:
        winner_not_found = True    

    return winner_not_found                      


main()