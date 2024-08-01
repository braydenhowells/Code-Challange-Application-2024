import random
import time

# validation arguments
yesno_validation = ['y', 'yes', 'n', 'no']
first_second_validation = '12'
player_move_validation = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# overall variables
number_of_wins = 0
number_of_losses = 0
first_game = True


# func for making sure that the user responses stay in bounds
def validate(player_input, validation_args):
    if player_input in validation_args:
        return True
    else:
        return False


# optionally starts a game, validates
def startup_loop():
    if first_game:
        start_choice = input('Begin? (y/n) ')
    else:
        start_choice = input('Want to give it another go? (y/n) ')
    if validate(start_choice.lower(), yesno_validation):
        if start_choice.lower() == 'y' or start_choice.lower() == 'yes':
            game_startup()
        else:
            goodbye()
    else:
        print('Uh-oh. I didn\'t recognize that response. Let\'s try again. '
              '(Possible responses: y, yes, Y, YES, Yes, n, no, NO, No)')
        startup_loop()


# choose to go first or second, validate
def game_startup():
    beginning_move_choice = input('Would you like to move first or second? (1/2) ')
    if validate(beginning_move_choice, first_second_validation):
        if beginning_move_choice == '1':
            player_turn(0, [1, 2, 3, 4, 5, 6, 7, 8, 9], player_move_validation)
        else:
            cpu_turn(0, [1, 2, 3, 4, 5, 6, 7, 8, 9], player_move_validation)
    else:
        print('Uh-oh. I didn\'t recognize that response. Let\'s try again. '
              '(Possible responses include: 1, 2)')
        game_startup()


# show the grid, this is used after each turn
def display_grid(grid_icons):
    print(f'[{grid_icons[0]}] [{grid_icons[1]}] [{grid_icons[2]}]')
    print(f'[{grid_icons[3]}] [{grid_icons[4]}] [{grid_icons[5]}]')
    print(f'[{grid_icons[6]}] [{grid_icons[7]}] [{grid_icons[8]}]')


# we will use this to edit the list of possible moves for player and cpu
def delete(tic_tac_toe_choice, valids):
    new = []
    for item in valids:
        if not item == tic_tac_toe_choice:
            new.append(item)
    return new


# this covers all the possible endgame options
def check_win(grid_icons, team, turns):
    # rows
    if grid_icons[0] == team and grid_icons[1] == team and grid_icons[2] == team:
        return True
    elif grid_icons[3] == team and grid_icons[4] == team and grid_icons[5] == team:
        return True
    elif grid_icons[6] == team and grid_icons[7] == team and grid_icons[8] == team:
        return True
    # columns
    elif grid_icons[0] == team and grid_icons[3] == team and grid_icons[6] == team:
        return True
    elif grid_icons[1] == team and grid_icons[4] == team and grid_icons[7] == team:
        return True
    elif grid_icons[2] == team and grid_icons[5] == team and grid_icons[8] == team:
        return True
    # diagonally
    elif grid_icons[0] == team and grid_icons[4] == team and grid_icons[8] == team:
        return True
    elif grid_icons[6] == team and grid_icons[4] == team and grid_icons[2] == team:
        return True
    # tie
    elif turns == 9:
        results('tie')


def player_turn(turns, grid_icons, valids):
    display_grid(grid_icons)
    time.sleep(2)   # helps for readability
    tic_tac_toe_choice = input('Choose a number to make your move: ')
    if validate(tic_tac_toe_choice, valids):
        grid_icons[(int(tic_tac_toe_choice) - 1)] = 'X'
        new_valids = delete(tic_tac_toe_choice, valids)
        turns += 1

        if check_win(grid_icons, 'X', turns):
            display_grid(grid_icons)
            results('player')

        else:
            cpu_turn(turns, grid_icons, new_valids)
    else:
        print(f'That won\'t work! Available responses:')
        print(valids)
        player_turn(turns, grid_icons, valids)


def cpu_turn(turns, grid_icons, valids):
    display_grid(grid_icons)
    time.sleep(2)   # helps for readability
    cpu_choice = random.choice(valids)
    print(f'MY TURN! I CHOOSE LUCKY NUMBER {cpu_choice}!')
    grid_icons[int(cpu_choice) - 1] = 'O'
    new_valids = delete(cpu_choice, valids)
    turns += 1
    if check_win(grid_icons, 'O', turns):
        display_grid(grid_icons)
        results('cpu')
    else:
        player_turn(turns, grid_icons, new_valids)


# overall results / playful game feedback
def results(winner):
    global number_of_wins
    global number_of_losses
    if winner == 'player':
        print('Congrats, you win!')
        print('YOU MUST HAVE CHEATED. I WANT A REMATCH.')
        number_of_wins += 1
    elif winner == 'cpu':
        print('Bummer. Better luck next time! You can always try again.')
        print('HA! HOW DOES IT FEEL?')
        number_of_losses += 1
    else:
        print('Oops! You tied.')
    global first_game
    first_game = False
    print('###########################################')
    print(f'{player_name}\'s score: {number_of_wins}')
    print(f'Kyle\'s score: {number_of_losses}')
    startup_loop()


def goodbye():
    if first_game:
        print(f'Thanks for nothing, {player_name}!')    # cheeky response option
    else:
        print(f'Thanks for playing, {player_name}!')    # program closes after this


# program startup block
player_name = input('Welcome to Tic Tac Toe. What is your name? ')
print(f'NICE TO MEET YOU, {player_name}. '
      'YOU CAN CALL ME KYLE. IT IS UNLIKELY THAT YOU WILL EVER BEAT ME, '
      'BUT YOU CAN TRY!')
startup_loop()
