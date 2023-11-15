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
    pass