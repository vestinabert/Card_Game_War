class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self):
        return self.hand.pop(0) if self.hand else None