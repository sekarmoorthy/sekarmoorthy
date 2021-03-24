from os import system
import random
def game_table(tablebox):
    system('cls')
    print(tablebox[7]+"|"+tablebox[8]+"|"+tablebox[9])
    print("-----")
    print(tablebox[4]+"|"+tablebox[5]+"|"+tablebox[6])
    print("-----")
    print(tablebox[1]+"|"+tablebox[2]+"|"+tablebox[3])
def place_marker(tablebox,marker,positionvalue):
    tablebox[positionvalue] = marker
def valueinput():
    n=0
    while n not in [1,2,3,4,5,6,7,8,9] or not space_check(tablebox,n):
        n = int(input(f'Enter the positon for where to place : '))
    return n
def player_input():
    marker = ''
    while marker !='x' and marker !='o':
        marker = input('Player1 : choose x or o : ')
        marker.upper();
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
def space_check(tablebox,positionvalue):
    return tablebox[positionvalue] == ' '
def full_board_check(tablebox):
    for i in range(1,10):
        if space_check(tablebox,i):
            return False
    return True
def winner_check(tablebox,mark):
    if  ((tablebox[1] == tablebox[2] == tablebox[3] == mark) or 
        (tablebox[1] == tablebox[5] == tablebox[9] == mark) or
        (tablebox[1] == tablebox[4] == tablebox[7] == mark) or
        (tablebox[3] == tablebox[6] == tablebox[9] == mark) or
        (tablebox[3] == tablebox[5] == tablebox[7] == mark) or
        (tablebox[7] == tablebox[8] == tablebox[9] == mark) or
        (tablebox[4] == tablebox[5] == tablebox[6] == mark) or
        (tablebox[2] == tablebox[5] == tablebox[8] == mark)):
        print("player 1 is the winner")
        return True
    
def replay():
    responce = input("Play again? Enter Yes or No : ")
    return responce == 'Yes'
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
while True:
    tablebox = [" "]*10
    player1,player2 = player_input()
    turn = choose_first()
    print(turn + " Will go First")
    play_game = input("Ready to play? y or n :")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            game_table(tablebox)
            position = valueinput()
            place_marker(tablebox,player1,position)
            if (winner_check(tablebox,player1)==True):
                game_table(tablebox)
                print('Player 1 Has Won !!')
                game_on = False
            else:
                if full_board_check(tablebox):
                    game_table(tablebox)
                    print('Tie Game !!')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            game_table(tablebox)
            position = valueinput()
            place_marker(tablebox,player2,position)
            if (winner_check(tablebox,player2)==True):
                game_table(tablebox)
                print('Player 2 Has Won !!')
                game_on = False
            else:
                if full_board_check(tablebox):
                    game_table(tablebox)
                    print('Tie Game !!')
                    game_on = False
                else:
                    turn = 'Player 1'
            
    if not replay():
        break
