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
        self.game_loop()

    def game_loop(self):
        while True:
            self.round += 1
            self.game_round()

    def game_round(self):
        player_card = self.player1.draw_card()
        cpu_card = self.player2.draw_card()
        outcome = player_card.compare_to(cpu_card)
        if outcome == 0:
            #war
            ...
        elif outcome > 0:
            #player wins
            self.round_outcome([player_card, cpu_card], self.player1)
        elif outcome < 0:
            #cpu wins
            self.round_outcome([player_card, cpu_card], self.player2)

    def round_outcome(self, cards, winner: Player):
        for card in cards:
            winner.add_card(card)

