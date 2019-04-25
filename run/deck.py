

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
                if value == 10:
                    value = 'T'
                elif value == 11:
                    value = 'J'
                elif value == 12:
                    value = 'Q'
                elif value == 13:
                    value = 'K'
                elif value == 1:
                    value = 'A'
                self.cards.append(Card(suit,value))
    
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i],self.cards[r] = self.cards[r],self.cards[i]

    def show(self):
        print([card.show() for card in self.cards])

deck = Deck()
deck.shuffle()
deck.show()