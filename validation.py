def validate_game_mode():
    while True:
        game_mode = input("Do you want to play Full War Game (f) or Quick War Game (q)? ").strip().lower()
        if game_mode == 'f' or game_mode == 'q':
            return game_mode
        else:
            print("Invalid input! Please enter 'f' for Full War Game or 'q' for Quick War Game.")

def validate_player_name(player_num):
    while True:
        player_name = input(f"Enter Player {player_num} name: ").strip()
        if player_name:
            return player_name
        else:
            print(f"Player {player_num} name cannot be empty. Please try again.")

def validate_rounds():
    while True:
        try:
            rounds = int(input("Enter number of rounds: ").strip())
            if rounds <= 0:
                raise ValueError("Number of rounds must be a positive integer.")
            return rounds
        except ValueError as e:
            print(f"Invalid input! {e}")