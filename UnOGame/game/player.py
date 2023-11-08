
from game.card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        card = deck.draw_card()
        self.hand.append(card)

    def play_card(self, card_index):
        card = self.hand.pop(card_index)
        return card

    def has_won(self):
        return len(self.hand) == 0
