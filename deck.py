from random import shuffle
class Deck:
    cards = []
    
    @staticmethod
    def shuffle_cards(cls):
        shuffle(cls.cards)
        