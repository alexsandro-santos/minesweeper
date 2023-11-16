difficulty = {"easy": (10, 20), "medium": (16, 35), "hard": (20, 50)}


def read_player_difficulty():
    while True:
        choice = input("Choose complexity between 'easy', 'medium' or 'hard':")
        if choice in {"easy", "medium", "hard"}:
            break
        else:
            print("Valid choice, please")

    n, n_bombs = difficulty[choice]

    return n, n_bombs


def read_player_command():
    while True:
        cmd = input("Choose move between 'o' for open, 'f' for flag or '?':")
        if cmd in {"o", "f", "?"}:
            break
        else:
            print("Valid choice, please")

    return cmd


def read_player_coordinate(n):
    while True:
        choice = input(f"Choose coordinates between 1 and {n}:")
        try:
            choice = int(choice)
        except Exception:
            print("Valid choice, please") 
            continue
        if 1 <= choice <= n:
            break
        else:
            print("Valid choice, please")

    return choice - 1
