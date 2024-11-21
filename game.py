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

    def play_round(self):
        self.round += 1
        print(f"Round {self.round}:")

        card1 = self.player1.draw_card()
        card2 = self.player2.draw_card()

        if not card1 or not card2:
            print("The game is over. No cards left to play.")
            return False

        print(f"{self.player1.name} plays: {card1}")
        print(f"{self.player2.name} plays: {card2}")

        comparison = card1.compare_to(card2)

        if comparison > 0:
            self.player1.add_card(card1)
            self.player1.add_card(card2)
            print(f"{self.player1.name} wins this round.")
        elif comparison < 0:
            self.player2.add_card(card1)
            self.player2.add_card(card2)
            print(f"{self.player2.name} wins this round.")
        else:
            print("It's a tie! Both players place 3 cards face down and reveal another card.")
            if len(self.player1.hand) < 4 or len(self.player2.hand) < 4:
                print("Not enough cards for a war!")
                return False
            war_cards1 = [card1] + [self.player1.draw_card() for _ in range(3)]
            war_cards2 = [card2] + [self.player2.draw_card() for _ in range(3)]
            print(f"{self.player1.name} plays: {war_cards1[-1]}")
            print(f"{self.player2.name} plays: {war_cards2[-1]}")

            war_comparison = war_cards1[-1].compare_to(war_cards2[-1()])
            if war_comparison > 0:
                self.player1.hand.extend(war_cards1 + war_cards2)
                print(f"{self.player1.name} wins the war!")
            elif war_comparison < 0:
                self.player2.hand.extend(war_cards1 + war_cards2)
                print(f"{self.player2.name} wins the war!")
            else:
                print("War is also a tie!")
                return False

        return True

    def check_winner(self):
        if not self.player1.has_cards():
            return f"{self.player2.name} wins the game!"
        elif not self.player2.has_cards():
            return f"{self.player1.name} wins the game!"
        return None
