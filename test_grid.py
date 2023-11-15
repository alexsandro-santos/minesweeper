from game_minesweeper.grid_minesweeper import *
from game_minesweeper.textual_minesweeper import *

game_grid, state_grid = game_grid_create()

game_grid = place_bombs(game_grid)

print(get_tile_neighbours(game_grid, 1, 2))

print(grid_to_string(game_grid))

game_grid = tile_number_calculate(game_grid)

print('\n'+grid_to_string(game_grid))