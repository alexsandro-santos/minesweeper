import os

from game_minesweeper.grid_minesweeper import *
from game_minesweeper.textual_minesweeper import *

# n, n_bombs = read_player_difficulty()
# game_grid, state_grid = game_grid_init(n)

# os.system("cls" if os.name == "nt" else "clear")
# print(grid_to_string(state_grid))

# while not is_game_over(state_grid, n_bombs):
#     move = read_player_command()
#     coordinate_x = read_player_coordinate(game_grid)
#     coordinate_y = read_player_coordinate(game_grid)

#     state_grid = make_move(game_grid, state_grid, move, coordinate_x, coordinate_y)

#     os.system("cls" if os.name == "nt" else "clear")
#     print(grid_to_string(state_grid))

# game_grid, state_grid = game_grid_create()
# game_grid = place_bombs(game_grid)
# game_grid = tile_number_calculate(game_grid)

# game_grid = [
#     [0, 0,-1,0],
#     [-1,0, 0,0],
#     [0, 0, 0,0],
#     [0, 0, 0,0],
#     [0, 0,0,-1]
# ]
# # state_grid = [[' ' for i in range(4)] for i in range(5)]
# game_grid = tile_number_calculate(game_grid)

# print(grid_to_string(game_grid))
# print(get_all_tiles(game_grid))
# # print('\n'+grid_to_string(state_grid))
# # print(get_tile_neighbours(game_grid, 3, 0))
# # print(get_neighbours_to_open(game_grid, 3, 0))
# # print(get_neighbours_to_open(game_grid, 1, 1))
# # print(get_neighbours_to_open(game_grid, 2, 0))

# state_grid = open_tiles(game_grid, state_grid, 2, 0)

# print(grid_to_string(state_grid))

game_play()