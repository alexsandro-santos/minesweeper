from api_minesweeper import *


def main():
    n, n_bombs, root, state_grid = start_game()
    if n>0:
        play_game(n, n_bombs, root, state_grid)
        root.mainloop()

if __name__ == '__main__':
    main()
