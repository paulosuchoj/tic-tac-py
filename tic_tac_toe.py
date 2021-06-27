import random

player_choice = ''
computer_choice = ''
game_won = False


def start_game():
    global player_choice, computer_choice

    print('Welcome to Tic-Tac-Toe!')

    while True:
        try:
            player_choice = input('Do you want to be O or X?\n')
        except ValueError:
            print('''Sorry, I don't understand what you typed!''')
            continue

        if not (player_choice == 'X' or player_choice == 'O'):
            print('You must choose either X or O!')
            continue
        else:
            break

    if player_choice == 'X':
        print('\nPlayer will be X and Computer will be O!\n')
        computer_choice = 'O'
    else:
        print('\nPlayer will be O and Computer will be X!\n')
        computer_choice = 'X'


board = {'top_L': '', 'top_M': '', 'top_R': '',
         'mid_L': '', 'mid_M': '', 'mid_R': '',
         'bottom_L': '', 'bottom_M': '', 'bottom_R': ''}


def player_play(board):
    while True:
        try:
            play_position = input(
                'Where do you want to play? You can choose the board position by typing top_x, mid_x, or bottom_x, where x is either L, M or R (for left, middle and right positions).\n')
        except ValueError:
            print('''Sorry, I don't understand what you typed!\n''')
            continue

        if play_position not in ['top_L', 'top_M', 'top_R', 'mid_L', 'mid_M', 'mid_R', 'bottom_L', 'bottom_M', 'bottom_R']:
            print('Please select a valid position\n')
            continue
        else:
            if board[play_position] == '':
                board[play_position] = player_choice
                break
            else:
                print('That position is already occupied! Please choose another one.')
                player_play(board)

    print_board()


def random_play(board):
    keys = list(board.keys())
    random.shuffle(keys)

    for key in keys:
        if board[key] == '':
            board[key] = computer_choice
            print('Computer plays in ' + key)
            break

    print_board()


def print_board():
    print('\n' + board['top_L'] + '|' + board['top_M'] + '|' + board['top_R'])
    print('-+-+-')
    print(board['mid_L'] + '|' + board['mid_M'] + '|' + board['mid_R'])
    print('-+-+-')
    print(board['bottom_L'] + '|' +
          board['bottom_M'] + '|' + board['bottom_R'] + '\n')


def check_win(board):
    global game_won

    # Game won by filling top row
    if (board['top_L'] == computer_choice and board['top_M'] == computer_choice and board['top_R'] == computer_choice):
        game_won = True
        print('Computer ' + computer_choice + ' wins!')
        print_board()
    elif (board['top_L'] == player_choice and board['top_M'] == player_choice and board['top_R'] == player_choice):
        game_won = True
        print('Player ' + player_choice + ' wins!')
        print_board()

    # Game won by filling middle row
    if (board['mid_L'] == computer_choice and board['mid_M'] == computer_choice and board['mid_R'] == computer_choice):
        game_won = True
        print('Computer ' + computer_choice + ' wins!')
        print_board()
    elif (board['mid_L'] == player_choice and board['mid_M'] == player_choice and board['mid_R'] == player_choice):
        game_won = True
        print('Player ' + player_choice + ' wins!')
        print_board()

    # Game won by filling bottom row
    if (board['bottom_L'] == computer_choice and board['bottom_M'] == computer_choice and board['bottom_R'] == computer_choice):
        game_won = True
        print('Computer ' + computer_choice + ' wins!')
        print_board()
    elif (board['bottom_L'] == computer_choice and board['bottom_M'] == computer_choice and board['bottom_R'] == computer_choice):
        game_won = True
        print('Player ' + player_choice + ' wins!')
        print_board()

    # Game won by filling left column
    if (board['top_L'] == computer_choice and board['mid_L'] == computer_choice and board['bottom_L'] == computer_choice):
        game_won = True
        print('Computer ' + computer_choice + ' wins!')
        print_board()
    elif (board['top_L'] == computer_choice and board['mid_L'] == computer_choice and board['bottom_L'] == computer_choice):
        game_won = True
        print('Player ' + player_choice + ' wins!')
        print_board()

    # Game won by filling middle column
    if (board['top_M'] == computer_choice and board['mid_M'] == computer_choice and board['bottom_M'] == computer_choice):
        print('Computer ' + computer_choice + ' wins!')
        print_board()
    elif (board['top_M'] == computer_choice and board['mid_M'] == computer_choice and board['bottom_M'] == computer_choice):
        game_won = True
        print('Player ' + player_choice + ' wins!')
        print_board()

    # Game won by filling right column
    if (board['top_R'] == computer_choice and board['mid_R'] == computer_choice and board['bottom_R'] == computer_choice):
        print('Computer ' + computer_choice + ' wins!')
        print_board()
    elif (board['top_R'] == computer_choice and board['mid_R'] == computer_choice and board['bottom_R'] == computer_choice):
        game_won = True
        print('Player ' + player_choice + ' wins!')
        print_board()

    # Game won by filling diagonally from top left
    if (board['top_L'] == computer_choice and board['mid_M'] == computer_choice and board['bottom_R'] == computer_choice):
        print('Computer ' + computer_choice + ' wins!')
        print_board()
    elif (board['top_L'] == computer_choice and board['mid_M'] == computer_choice and board['bottom_R'] == computer_choice):
        game_won = True
        print('Player ' + player_choice + ' wins!')
        print_board()

    # Game won by filling diagonally from top right
    if (board['top_R'] == computer_choice and board['mid_M'] == computer_choice and board['bottom_L'] == computer_choice):
        print('Computer ' + computer_choice + ' wins!')
        print_board()
    elif (board['top_R'] == computer_choice and board['mid_M'] == computer_choice and board['bottom_L'] == computer_choice):
        game_won = True
        print('Player ' + player_choice + ' wins!')
        print_board()


def check_draw(board):
    global game_won

    if (board['top_L'] != '' and board['top_M'] != '' and board['top_R'] != '' and board['mid_L'] != '' and board['mid_M'] != '' and board['mid_R'] != '' and board['bottom_L'] != '' and board['bottom_M'] != '' and board['bottom_R'] != ''):
        game_won = True
        print('The board has been filled, and the game has ended in a draw!')


def run_game():
    while game_won == False:
        player_play(board)
        check_win(board)
        check_draw(board)
        random_play(board)
        check_win(board)
        check_draw(board)


start_game()
run_game()
