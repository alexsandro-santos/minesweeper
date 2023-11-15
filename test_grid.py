from game_minesweeper.grid_minesweeper import *
from game_minesweeper.textual_minesweeper import *

game_grid , state_grid = game_grid_create()
print(state_grid)

bombs = get_bombs_positions(game_grid)
print(bombs)

game_grid = place_bombs(game_grid)
print(game_grid)

print(grid_to_string(game_grid))