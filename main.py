from game import Game

def run_game():
    print("Welcome to the War Card Game!")
    rounds = input("How many round do you want to play? ")
    player1_name = input("Enter Player 1 name: ")
    player2_name = "Computer"

    game = Game(player1_name, player2_name, rounds)
    
    game.start_game()

    # print("Player 1 Info:", game.player1.__dict__)
    # print("Player 2 Info:", game.player2.__dict__)
    
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
