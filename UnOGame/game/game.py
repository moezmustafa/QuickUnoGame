
import random

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        colors = ["red", "blue", "green", "yellow"]
        values = [str(i) for i in range(10)] + ["Skip", "Reverse", "Draw Two"]
        for color in colors:
            for value in values:
                self.cards.append(Card(color, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw_card())

    def play(self, card):
        self.hand.remove(card)

class Game:
    def __init__(self, *players):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = players
        self.current_player = 0
        self.direction = 1
        self.played_card = None
        self.play_game()

    def play_game(self):
        while True:
            print(f"\nCurrent card: {self.played_card.color} {self.played_card.value}")
            print(f"Current player: {self.players[self.current_player].name}")
            self.players[self.current_player].draw(self.deck)
            self.show_hand()
            card = self.get_play()
            self.players[self.current_player].play(card)
            self.played_card = card
            if len(self.players[self.current_player].hand) == 0:
                print(f"{self.players[self.current_player].name} wins!")
                break
            self.current_player = (self.current_player + self.direction) % len(self.players)

    def show_hand(self):
        print(f"{self.players[self.current_player].name}'s hand:")
        for card in self.players[self.current_player].hand:
            print(f"{card.color} {card.value}")

    def get_play(self):
        while True:
            play = input("Enter the card you want to play: ")
            color, value = play.split()
            for card in self.players[self.current_player].hand:
                if card.color == color and card.value == value:
                    return card
            print("Invalid card. Try again.")

if __name__ == "__main__":
    player1 = Player("Alice")
    player2 = Player("Bob")
    game = Game(player1, player2)
