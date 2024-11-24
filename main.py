from game import Game

def run_game():
    print("Welcome to the War Card Game!")
    
    while True:
        game_mode = input("Do you want to play Full War Game (f) or Quick War Game (q)? ").strip().lower()
        
        if game_mode == 'f' or game_mode == 'q':
            break
        else:
            print("Invalid input! Please enter 'f' for Full War Game or 'q' for Quick War Game.")
    
    while True:
        player1_name = input("Enter Player 1 name: ").strip()
        
        if player1_name:
            break
        else:
            print("Player 1 name cannot be empty. Please try again.")
    
    player2_name = "Computer"

    try:
        if game_mode == 'f':
            game = Game(player1_name, player2_name)
        elif game_mode == 'q':
            while True:
                try:
                    rounds = int(input("Enter number of rounds: ").strip())
                    if rounds <= 0:
                        raise ValueError("Number of rounds must be a positive integer.")
                    game = Game(player1_name, player2_name, rounds)
                    break
                except ValueError as e:
                    print(f"Invalid input! {e}")
                    continue
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
