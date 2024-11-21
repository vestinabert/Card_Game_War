from deck import Deck
from player import Player

class Game:
    def __init__(self, player1_name, player2_name):
        self.deck = Deck()
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.round = 0

    def start_game(self):
        self.deck.shuffle()
        self.player1.hand = self.deck.deal(26)
        self.player2.hand = self.deck.deal(26)