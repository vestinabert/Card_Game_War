from game import Game

def run_game():
    print("Welcome to the War Card Game!")
    game_mode = input("Do you want to play Full War Game (f) or Quick War Game (q)? ")

    player1_name = input("Enter Player 1 name: ")
    player2_name = "Computer"
    
    if game_mode.strip() == "f":
        game = Game(player1_name, player2_name)

    elif game_mode.strip() == "q":
        rounds = input("Enter number of rounds: ")
        game = Game(player1_name, player2_name, rounds)
    
    game.start_game()
    
    while True:
        keep_playing = game.play_round()

        if not keep_playing:
            break

        if game.is_game_over():
            break

    winner = game.check_winner()
    print(winner)

if __name__ == "__main__":
    run_game()
