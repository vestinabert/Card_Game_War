from game import Game
from validation import validate_game_mode, validate_player_name, validate_rounds
import pyfiglet


def run_game():
    ascii_art = pyfiglet.figlet_format("Welcome to the War Card Game!")
    print(ascii_art)

    game_mode = validate_game_mode()

    player1_name = validate_player_name(1)
    player2_name = "Computer"

    try:
        if game_mode == 'f':
            game = Game(player1_name, player2_name)
        elif game_mode == 'q':
            rounds = validate_rounds()
            game = Game(player1_name, player2_name, rounds)
    except Exception as e:
        print(f"Error creating the game: {e}")
        return

    game.start_game()

    while True:
        if game.is_game_over():
            break
        game.play_round()

    game.check_winner()


if __name__ == "__main__":
    run_game()
