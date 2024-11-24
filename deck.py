import random
from card import Card

class Deck:
    """
    Represents a standard 52-card deck of playing cards.

    Attributes:
        cards (list): A list of Card objects representing the deck.

    Methods:
        shuffle(): Shuffles the deck randomly.
        deal(num_cards): Deals a specified number of cards from the deck.
    """

    def __init__(self):
        """
        Initializes a Deck instance with 52 cards.
        """
        self.cards = []  # List to hold Card objects.
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        # ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        ranks = ['Jack', 'Queen', 'King', 'Ace']
        # Generate all 52 cards and add them to the deck.
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        """
        Deals a specified number of cards from the top of the deck.

        Returns:
            list: A list of Card objects dealt from the deck.
        """
        hand = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return hand
