class Card:
    def __init__(self, suit: str, rank: str):
        self._suit = suit.title()
        self._rank = rank.title()

    def __str__(self):
        return f"{self._rank} of {self._suit}"
    
