

import os
import graphics

from view import Menu
from deck import Deck

BUY_IN = 200

def holdem():
    #display game banner
    Menu.start()
    input('\nPress any key to start.')
    #start
    os.system('clear')
    #set pot
    player_pots = [BUY_IN,BUY_IN]
    total_pot   = 0
    while player_pots[0] > 0 or player_pots[1] > 0:
        Menu.start()
        #initalize deck
        deck = Deck()
        deck.shuffle()
        #set hold cards
        player_hand   = deck.deal('player_hand')
        computer_hand = deck.deal('computer_hand')
        #set board cards
        flop  = deck.deal('flop')
        turn  = deck.deal('turn')
        river = deck.deal('river')
        graphics.game_board(player_pots, player_hand)
        option = input('\nEnter Option: ')
        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3: 
            break


if __name__ == "__main__":
    holdem()


