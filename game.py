from deck import Deck
from player import Player
import sys

class Game:
    """
    Represents a card game between two players.

    Attributes:
        deck (Deck): The deck of cards used for the game.
        player1 (Player): The first player in the game.
        player2 (Player): The second player in the game.
        round (int): The current round number of the game.
        _max_rounds (int): The maximum number of rounds, or None if there is no round limit.

    Methods:
        start_game(): Shuffles the deck and deals cards to both players.
        play_round(): Plays one round of the game, comparing cards and managing the result.
        handle_war(): Handles the war scenario when a tie occurs.
        check_winner(): Determines the winner of the game based on rounds or card count.
        is_game_over(): Checks whether the game is over based on rounds or cards remaining.
    """

    def __init__(self, player1_name: str, player2_name: str, max_rounds: int = None) -> None:
        """
        Initializes the Game instance with a deck, two players, and a round counter.
        The game will continue indefinitely until a player runs out of cards if max_rounds is None.
        """
        self.deck = Deck()
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.round = 0

        if max_rounds:
            try:
                self._max_rounds = int(max_rounds)
                if self._max_rounds <= 0:
                    raise ValueError("max_rounds must be a positive integer.")
            except ValueError as e:
                print(f"Error: {e}")
                sys.exit(1)
        else:
            self._max_rounds = None


    def start_game(self) -> None:
        """
        Prepares the game by shuffling the deck and dealing 26 cards to each player.
        """
        self.deck.shuffle()
        self.player1.hand = self.deck.deal(8)
        self.player2.hand = self.deck.deal(8)

    def play_round(self) -> None:
        """
        Plays one round of the game, comparing the top card of both players.
        Returns True if the round was played successfully, False if the game ends.
        """
        self.round += 1
        
        print(f"Round {self.round}:     --------------------{len(self.player1.hand)} vs {len(self.player2.hand)}---------------------")

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
            self.handle_war([card1], [card2])

    def handle_war(self, player1_card: list, player2_card: list) -> None:
        """
        Handles the war scenario where both players play tied cards.
        Each player places 1 card face down and reveals another.
        """
        while len(self.player1.hand) >= 2 and len(self.player2.hand) >= 2:
            print("It's a tie! Both players place 1 card face down and reveal another card.")
            war_cards1 = player1_card + [self.player1.draw_card() for _ in range(2)]
            war_cards2 = player2_card + [self.player2.draw_card() for _ in range(2)]
            print(f"{self.player1.name} plays: {war_cards1[-1]}")
            print(f"{self.player2.name} plays: {war_cards2[-1]}")

            war_comparison = war_cards1[-1].compare_to(war_cards2[-1])
            if war_comparison > 0:
                self.player1.hand.extend(war_cards1 + war_cards2)
                print(f"{self.player1.name} wins the war!")
                return
            elif war_comparison < 0:
                self.player2.hand.extend(war_cards1 + war_cards2)
                print(f"{self.player2.name} wins the war!")
                return
            else:
                player1_card = war_cards1
                player2_card = war_cards2

        print("Not enough cards for a war!")
        self.check_winner()
       

    def is_game_over(self) -> bool:
        """
        Checks if the game is over. The game can end in two ways:
        1. A round limit is reached.
        2. One player has no cards left.
        """
        if self._max_rounds and self.round >= self._max_rounds:
            return True
        if self.round > 100:
            print("Game is taking too long. Ending the game.")
            return True
        elif not self._max_rounds and (not self.player1.has_cards() or not self.player2.has_cards()):
            return True
        return False

    def check_winner(self) -> str:
        """
        Checks the winner of the game based on the remaining cards or rounds.
        If no rounds limit, it checks who has more cards remaining.
        """

        if len(self.player1.hand) > len(self.player2.hand):
            print (f"{self.player1.name} wins the game!")
        elif len(self.player2.hand) > len(self.player1.hand):
            print  (f"{self.player2.name} wins the game!")
        else:
            print ("It's a tie! No winner.")
        sys.exit(1)
