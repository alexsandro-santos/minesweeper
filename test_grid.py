import os

from game_minesweeper.grid_minesweeper import *
from game_minesweeper.textual_minesweeper import *

game_grid, state_grid = game_grid_init()

os.system("cls" if os.name == "nt" else "clear")
print(grid_to_string(state_grid))

while not is_game_over(game_grid, state_grid):
    move = read_player_command()
    coordinate_x = read_player_coordinates(game_grid)
    coordinate_y = read_player_coordinates(game_grid)

    state_grid = make_move(game_grid, state_grid, move, coordinate_x, coordinate_y)

    os.system("cls" if os.name == "nt" else "clear")
    print(grid_to_string(state_grid))