class Card:
    """
    Represents a single playing card with a suit and rank.
    
    Attributes:
        _suit (str): The suit of the card (e.g., "Hearts", "Diamonds").
        _rank (str): The rank of the card (e.g., "2", "Jack", "Ace").
    
    Methods:
        __str__(): Returns a user-friendly string representation of the card.
        __repr__(): Returns a developer-friendly string representation of the card.
        compare_to(other_card): Compares this card to another card based on rank values.
    """

    def __init__(self, suit: str, rank: str):
        self._suit = suit.title()  # Ensures the suit is stored in title case.
        self._rank = rank.title()  # Ensures the rank is stored in title case.

    def __str__(self):
        return f"{self._rank} of {self._suit}"
    
    def __repr__(self):
        return f"Card(rank={self._rank}, suit={self._suit})"
    
    def compare_to(self, other_card):
        """
        Compares this card to another card based on rank values.
        
        Returns:
            int: A positive number if this card is of higher rank,
                 a negative number if the other card is of higher rank,
                 or zero if the ranks are equal.
        """
        card_values = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12,
            'King': 13, 'Ace': 14
        }
        return card_values[self._rank] - card_values[other_card._rank]
