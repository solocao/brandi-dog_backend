import random

from card import Card
class Deck():

    def __init__(self, seed):
        if seed:
            random.seed(seed)

        self.N = 0

        self.cards = []
        
        values = ['A', 'K', 'Q', 'Ja', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        colors = ['clubs', 'diamonds', 'hearts', 'spades']
        for value in values: # go through all card values except the Joker
            for color in colors: # go through all 4 colors
                for _ in range(2): # playing with two decks
                    self.cards.append(Card( value, color, self.N))
                    self.N += 1

        # add the 6 jokers
        for _ in range(6):
            self.cards.append(Card('Jo', 'Jo', self.N))
            self.N += 1

        random.shuffle(self.cards) # shuffle the deck

    def give_card(self):
        return self.cards.pop(0)