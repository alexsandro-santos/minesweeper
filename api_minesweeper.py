from interface_minesweeper import interface_minesweeper as gui_ms
from game_minesweeper import grid_minesweeper as grid_ms
from game_minesweeper.textual_minesweeper import difficulty

def open_all(state_grid, game_grid):
    for i, row in enumerate(state_grid):
            for j, tile in enumerate(row):
                if tile not in ('?','f', ' '):
                    gui_ms.open_button(i,j,state_grid, game_grid)

def start_game():
    global diff
    root = gui_ms.startup()
    root.wait_variable(gui_ms.diff)
    if gui_ms.diff.get() == 'close':
        root.destroy()
        return 0,0,0,0
    else:
        n, n_bombs = difficulty[gui_ms.diff.get()]
        _, state_grid = grid_ms.game_grid_create(n)
        return n, n_bombs, root, state_grid

def play_game(n, n_bombs, root, state_grid):
    window_open = False
    gui_ms.create_grid_gui(root, state_grid,
                           lambda n=n, n_bombs=n_bombs,
                           root = root, state_grid = state_grid:
                           play_game(n,n_bombs,root,state_grid))
    root.wait_variable(gui_ms.x)
    if gui_ms.x.get()>0:
        #print(gui_ms.x.get(),gui_ms.y.get())
        click_x = gui_ms.x.get()
        click_y = gui_ms.y.get()
        game_grid, state_grid = grid_ms.game_grid_init(n, n_bombs, (click_x, click_y))
        state_grid = grid_ms.make_move(game_grid, state_grid, 'o', click_x, click_y)
        gui_ms.open_button(click_x,click_y,state_grid, game_grid)
        open_all(state_grid, game_grid)
        window_open = True
    game_over = grid_ms.is_game_over(state_grid, n_bombs)
    while ((not game_over) and window_open) :
        root.wait_variable(gui_ms.x)
        if gui_ms.x.get() > 0:
            cmd = 'o' ## receive from gui
            coordinate_x = gui_ms.x.get() ## receive from gui
            coordinate_y = gui_ms.y.get() ## receive from gui
            state_grid = grid_ms.make_move(game_grid, state_grid, cmd, coordinate_x, coordinate_y)
            open_all(state_grid, game_grid)
            game_over = grid_ms.is_game_over(state_grid, n_bombs)
        else:
            window_open = False
    
    if not window_open:
        print('\nGame closed before the end') # change a state to show endgame status
    elif -1 not in grid_ms.get_all_tiles(state_grid):
        print('\nYou won!') # change a state to show endgame status
        gui_ms.rb['text'] = gui_ms.winface
    else:
        print('\nYou lost!') # change a state to show endgame status

if __name__ == '__main__':
    n, n_bombs, root, state_grid = start_game()
    if n>0:
        play_game(n, n_bombs, root, state_grid)
        root.mainloop()
