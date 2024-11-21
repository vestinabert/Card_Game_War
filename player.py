class Player:
    """
    Represents a player in a card game.
    
    Attributes:
        name (str): The name of the player.
        hand (list): A list of Card objects representing the player's hand.
    
    Methods:
        draw_card(): Removes and returns the top card from the player's hand.
        add_card(card): Adds a card to the player's hand.
        has_cards(): Checks if the player has any cards left in their hand.
    """

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self):
        """
        Removes and returns the top card from the player's hand.

        Returns:
            Card or None: The top card from the hand if available, or None if the hand is empty.
        """
        return self.hand.pop(0) if self.hand else None

    def add_card(self, card):
        """
        Adds a card to the player's hand.

        Args:
            card (Card): The card to be added to the player's hand.
        """
        self.hand.append(card)

    def has_cards(self):
        """
        Returns:
            bool: True if the player has cards in their hand, False otherwise.
        """
        return len(self.hand) > 0
