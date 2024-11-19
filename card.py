class Card:
    def __init__(self, suit: str, rank: str):
        self._suit = suit.title()
        self._rank = rank.title()

    def __str__(self):
        return f"{self._rank} of {self._suit}"
    
    def compare_to(self, other_card):
        values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "Jack":10, "Queen":11, "King":12}
        return values[self.rank]>values[other_card.rank]
    
