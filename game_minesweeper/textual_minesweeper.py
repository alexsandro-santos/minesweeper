def read_player_difficulty():
    while True:
        choice = input("Choose complexity between 'easy', 'medium' or 'hard':")
        try:
            choice = str(choice)
        except ValueError:
            print("Valid choice, please") 
            continue
        if choice in {"easy", "medium", "hard"}:
            break
        else:
            print("Valid choice, please")

    return choice

def read_player_command():
    while True:
        choice = input("Choose move between 'o' for open, 'f' for flag or '?':")
        try:
            choice = str(choice)
        except ValueError:
            print("Valid choice, please") 
            continue
        if choice in {"o", "f", "?"}:
            break
        else:
            print("Valid choice, please")

    return choice

def read_player_coordinates(game_grid):
    while True:
        choice = input(f"Choose coordinates between 1 and {len(game_grid)}:")
        try:
            choice = int(choice)
        except Exception:
            print("Valid choice, please") 
            continue
        if 1 <= choice <= len(game_grid):
            break
        else:
            print("Valid choice, please")

    return choice-1