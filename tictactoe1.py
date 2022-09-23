"""CSE210 Week1 Tic-Tac-Toe
   Kano Bailey

     The game of tic-tac-toe.
     2 players (x or o) pick the number on the game board to line "x" or "o" in 
     three consecutive row, column or diagonal line. 
"""

slot = [1,2,3,4,5,6,7,8,9]

def main():
    """Main function.
       It prints out a game board of number 1 to 9 first.
       It checks the turn of a player("x" or "o"), and ask for input.
       If a player is "x" and he/she choose a number from 1 to 9, it swaps the slot
       of the number with "x". If a player is "o", then it swaps with "o".
       The game continues until "x" or "o" manage to fill a row, a column or 3 slots diagonally,
       or players fill all the slots of the game board. If "x" or "o" wins, it print "x(or o)won!".
       If it's a tie, it prints out "It's a draw. Nice game!". 
   """

    # The game board with corresponding number 1 through 9 is printed.
    print_game_board()
    winner_not_found = True
    counter = 1

    # Main loop. The loop continues until the winner is found or the counter becomes 10.
    while winner_not_found and counter < 10:

        # A function to check if the player is "x" or "o".
        player = check_player(counter)

        # A function to have user input their choice number. It then checks if it's a valid
        # number (1 - 9)
        choice = check_input(player)

        # Actual swapping of a number with "x" or "o".
        if player == 'x':
            slot[choice-1] = 'x'
        else:
            slot[choice-1] = 'o'
    
        # A new game board with "x" or "o" is printed
        print_game_board()

        # checks to see if a winner is found.
        # if found, it prints out the name of the player　(x or o) with a message
        winner_not_found = winner_is(player)
        if winner_not_found == False:
            print(f"{player} won!")

        counter += 1

    # If the game is a draw (a winner is not found), it prints out a draw message.
    if winner_not_found == True:
        print(f"It's a draw. Nice game!")


def print_game_board():
    """Function to print out a game board.
       It is called every time a player picks a number. 
    """

    print(f"{slot[0]}|{slot[1]}|{slot[2]}")
    print(f"-+-+-")
    print(f"{slot[3]}|{slot[4]}|{slot[5]}")
    print(f"-+-+-")
    print(f"{slot[6]}|{slot[7]}|{slot[8]}")
    print()


def check_input(player):
    """Function to get an input and checks if the input is a valid number 1 through 9.
       argument: player (x or o)
       returns: choice (the valid input number)
       It checks if an input is a number, and if it is in the list slot to see if a number 
       chosen is not taken previously. if an input is not valid number, it asks to enter a
       valid number. If a number is valid, it returns the number.
    """

    choice = input(f"{player}'s turn to choose a square (1-9): ")
    while not(choice.isnumeric()) or (int(choice) not in slot):
        print("Please enter the valid number.")

        choice = input(f"{player}'s turn to choose a square (1-9): ")

    return int(choice)


def check_player(current_counter):
    """Function to check if a player is "x" or "o".
       argument: current_counter
       return:  player (x or o)
       An odd number turn is for x, and even number turn is for o.
    """

    turn_list = [1, 3, 5, 7, 9]
    
    # if the turn is odd number turn, it's x's turn. Otherwise it's O's turn.
    if current_counter in turn_list:
        player = 'x'
    else:
        player = 'o'
        
    return player           


def winner_is(player): 
    """Function to check if a winner if found.
       argument: player
       return:  winner_not_found flag
       It checks 3 consecutive slot in a row, column or diagonal line are taken by a 
       same player. If found, winner_not_found flag becomes True.  
    """

    
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

# Main function call
main()