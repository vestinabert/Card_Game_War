from deck import Deck
from player import Player

class Game:
    """
    Represents a card game between two players.

    Attributes:
        deck (Deck): The deck of cards used for the game.
        player1 (Player): The first player in the game.
        player2 (Player): The second player in the game.
        round (int): The current round number of the game.

    Methods:
        start_game(): Shuffles the deck and deals cards to both players.
    """

    def __init__(self, player1_name, player2_name):
        """
        Initializes the Game instance with a deck, two players, and a round counter.
        """
        self.deck = Deck()
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.round = 0

    def start_game(self):
        """
        Prepares the game by shuffling the deck and dealing 26 cards to each player.
        """
        self.deck.shuffle()
        self.player1.hand = self.deck.deal(26)
        self.player2.hand = self.deck.deal(26)
