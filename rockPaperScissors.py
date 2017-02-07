#! python3
""" This is a rock, paper, scissors game.
It includes a start menu, single and multiplayer versions of the game.
Both versions are 3 rounds. As of this build there is no score counter,
but I am looking into adding one."""

import random
import sys


def multiplayer():  # This is the code for a multiplayer version of rock, paper, scissors.
    player1 = input('Player 1 name: \n')
    player2 = input('Player 2 name: \n')
    for i in range(1, 4):
        # Want to find a way to hide user inputs.
        plyr1_choice = input(player1 + ' choose (r)ock, (p)aper, (s)cissors:\n')
        plyr2_choice = input(player2 + ' choose (r)ock, (p)aper, (s)cissors:\n')
        while plyr1_choice == 'r':
            if plyr2_choice == 'r':
                print('Draw!')
                break
            elif plyr2_choice == 'p':
                print('Paper beats rock! ' + player2 + ' wins!')
                break
            elif plyr2_choice == 's':
                print('Rock beats scissors! ' + player1 + ' wins!')
                break
        while plyr1_choice == 'p':
            if plyr2_choice == 'r':
                print('Paper beats rock! ' + player1 + ' wins!')
                break
            elif plyr2_choice == 'p':
                print('Draw!')
                break
            elif plyr2_choice == 's':
                print('Scissors beats paper! ' + player2 + ' wins')
                break
        while plyr1_choice == 's':
            if plyr2_choice == 'r':
                print('Rock beats scissors! ' + player2 + ' wins!')
                break
            elif plyr2_choice == 'p':
                print('Scissors beats paper! ' + player1 + ' wins')
                break
            elif plyr2_choice == 's':
                print('Draw!')
                break
    multi_replay()


def computer():
    for i in range(1, 4):
        comp = random.randint(1, 3)
        user = input('Rock, paper, scissors: \n')
        while comp == 1:
            if user == 'rock':
                print('Draw!')
            elif user == 'paper':
                print('Paper beats rock. You win!')
            elif user == 'scissors':
                print('Rock beats scissors. You lose!')
            break

        while comp == 2:
            if user == 'rock':
                print('Paper beats rock. You lose!')
            elif user == 'paper':
                print('Draw!')
            elif user == 'scissors':
                print('Scissors beats paper. You win!')
            break

        while comp == 3:
            if user == 'rock':
                print('Rock beats scissors. You win!')
            elif user == 'paper':
                print('Scissors beats paper. You lose!')
            elif user == 'scissors':
                print('Draw!')
            break
    replay()


def start():  # Basic start menu
    inp = input('(S)ingle or (m)ultiplayer:\n')
    if inp == 's':
        computer()
    elif inp == 'm':
        multiplayer()


def replay():  # Replay code for single player. Will probably join with multi_replay
    player = input('Play again? \n')
    if player == 'yes':
        computer()
    elif player == 'no':
        print('Goodbye')
    sys.exit()


def multi_replay():  # Replay code for multiplayer
    player = input('Play again? (Y)es or (n)o\n')
    if player == 'y':
        multiplayer()
    else:
        print('Goodbye')
    sys.end()


start()
