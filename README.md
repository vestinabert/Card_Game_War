# War Card Game

## Overview

This project implements the children's card game **War** using **Object-Oriented Programming (OOP)** principles. The game will be played between two players who take turns revealing cards from their deck, with the player having the highest card value winning the round. The goal is to be the first player to collect all the cards or have the most cards after a set number of rounds.

## Requirements

### Object-Oriented Programming (OOP)

The game must be implemented using **Object-Oriented Programming (OOP)** principles. The goal is to represent the core components of the game (cards, deck, players, etc.) as objects, each encapsulating its own data and behavior.

#### Key Classes and Responsibilities

1. **Card Class**:
   - Represents a single playing card.
   - Attributes: `rank` (e.g., 2-10, Jack, Queen, King, Ace) and `suit` (hearts, diamonds, clubs, spades).
   - Methods include:
     - `compare_to(other_card)` for comparing the card's rank with another card.
     - A method to display the card as a string (e.g., "Ace of Spades").

2. **Deck Class**:
   - Manages a collection of **Card** objects.
   - Responsible for shuffling, dealing cards to players, and tracking the remaining cards in the deck.
   - Methods should include:
     - `shuffle()` to randomize the order of the cards.
     - `deal(num_cards)` to deal a specified number of cards to players.
     - `size()` to return the number of cards remaining in the deck.

3. **Player Class**:
   - Represents a player in the game.
   - Attributes include the player's **name**.
   - Methods should include:
     - `draw_card()` to draw the top card from the player's hand.
     - `add_card(card)` to add a card to the player's hand.
     - `has_cards()` to check if the player still has cards.

4. **Game Class**:
   - Manages the overall game flow, including rounds, card comparisons, and victory conditions.
   - Responsible for initiating the game, handling the main loop, and determining the winner.
   - Methods should include:
     - `start_game()` to shuffle the deck and deal cards to players.
     - `play_round()` to process each round, compare cards, and determine the winner.
     - `handle_war()` to process "war" situations when both players have the same card value.
     - `check_winner()` to check if any player has collected all cards or reached the game-ending condition.


### Game Requirements
1. **Players**:
   - The game is played between two players, each having their own deck of cards.

2. **Gameplay**:
   - Players take turns revealing the top card of their deck.
   - The player with the highest card value wins the round and takes both cards.
   - In case of a tie, a "war" occurs where each player places one card face down and then reveals a card to determine the winner.
   - The game continues until one player collects all cards or after a specified number of rounds.

3. **Card Values**:
   - Cards have a rank (2-10, Jack, Queen, King, Ace) and a suit (hearts, diamonds, clubs, spades).
   - Face cards (Jack, Queen, King) have higher values than numbered cards, and Ace has the highest value.

4. **Game End**:
   - The game ends when one player collects all the cards.
   - Alternatively, the game can end after a set number of rounds, with the player holding the most cards at the end being declared the winner.

### User Interaction
- The game will be played through the **command line** interface.
- Players will be able to start a new game, view the current round, and see the results after each round.

### Features
- **User Input**: Allow players to choose between different game modes (e.g., classic War or a faster version).
- **Visual Representation**: Create a simple text-based UI or ASCII art to visually represent the game’s progress.
