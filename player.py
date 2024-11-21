class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self):
        return self.hand.pop(0) if self.hand else None
    
    def add_card(self, card):
        self.hand.append(card)

    def has_cards(self):
        return len(self.hand) > 0

