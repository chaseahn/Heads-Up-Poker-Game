

import random

class Card:
    def __init__(self,suit,val):
        self.suit = suit
        self.val  = val
    
    def show(self):
        return [self.suit,self.val] 

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for suit in ['♠','♥','♣','♦']:
            for value in range(1,14):
                self.cards.append(Card(suit,value))
    
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i],self.cards[r] = self.cards[r],self.cards[i]

    def deal(self,val):
        if val == 'player_hand':
            player_hand = [self.cards[0].show(),self.cards[2].show()]
            print(player_hand)
        elif val == 'computer_hand':
            computer_hand = [self.cards[1].show(),self.cards[3].show()]
            print(computer_hand)
        elif val == 'flop':
            flop = [self.cards[5].show(),self.cards[6].show(),self.cards[7].show()]
            print(flop)
        elif val == 'turn':
            flop = [self.cards[9].show()]
            print(flop)
        elif val == 'river':
            flop = [self.cards[11].show()]
            print(flop)
            
    def show(self):
        print([card.show() for card in self.cards])

deck = Deck()
deck.shuffle()
deck.show()
deck.deal('player_hand')
deck.deal('computer_hand')
deck.deal('flop')
deck.deal('turn')
deck.deal('river')