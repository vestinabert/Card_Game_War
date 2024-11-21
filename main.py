from game import Game

def run_game():
    print("Welcome to the War Card Game!")
    player1_name = input("Enter Player 1 name: ")
    player2_name = "Computer"

    game = Game(player1_name, player2_name)
    
    game.start_game()

    print("Player 1 Info:", game.player1.__dict__)
    print("Player 2 Info:", game.player2.__dict__)

if __name__ == "__main__":
    run_game()
