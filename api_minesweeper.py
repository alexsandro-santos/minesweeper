from interface_minesweeper import interface_minesweeper as gui_ms
from game_minesweeper import grid_minesweeper as grid_ms
from game_minesweeper.textual_minesweeper import difficulty


def open_all(state_grid, game_grid, x, y):
    for i, row in enumerate(state_grid):
        for j, tile in enumerate(row):
            if tile not in ('f','?',' ') or (i==x and j==y):
                gui_ms.open_button(i,j,'o',state_grid, game_grid)


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

    global mainFrame
    
    try: mainFrame.destroy()
    except: pass


    gui_ms.window_open = False
    mainFrame = gui_ms.create_grid_gui(root, state_grid,
                           lambda n=n, n_bombs=n_bombs,
                           root = root, state_grid = state_grid:
                           play_game(n,n_bombs,root,state_grid))
    
    root.wait_variable(gui_ms.x)
    if gui_ms.x.get()>=0:
        click_x = gui_ms.x.get()
        click_y = gui_ms.y.get()
        command = gui_ms.cmd.get()
        game_grid, state_grid = grid_ms.game_grid_init(n, n_bombs, (click_x, click_y))
        state_grid = grid_ms.make_move(game_grid, state_grid, command, click_x, click_y)
        if command == 'o':
            open_all(state_grid, game_grid, click_x, click_y)
        gui_ms.window_open = True

    while not grid_ms.is_game_over(state_grid, n_bombs) and gui_ms.window_open :
        root.wait_variable(gui_ms.x)
        if gui_ms.x.get() >= 0:
            coordinate_x = gui_ms.x.get() ## receive from gui
            coordinate_y = gui_ms.y.get() ## receive from gui
            command = gui_ms.cmd.get() ## receive from gui
            state_grid = grid_ms.make_move(game_grid, state_grid, command, coordinate_x, coordinate_y)
            if command == 'o':
                open_all(state_grid, game_grid, coordinate_x, coordinate_y)
        else:
            gui_ms.window_open = False
    
    if gui_ms.window_open:
        gui_ms.rb['bg']='yellow'
        b = gui_ms.Label(mainFrame, text='')
        b.grid(row=1,column=0, columnspan=5)
        if -1 not in grid_ms.get_all_tiles(state_grid):
            b['text'] = "You won!"
            gui_ms.rb['text'] = gui_ms.winface
            gui_ms.label_count['text'] = 0
        else:
            b['text'] = "You lose!"
            gui_ms.rb['text'] = gui_ms.sad
            gui_ms.label_count['text'] = n_bombs


if __name__ == '__main__':
    n, n_bombs, root, state_grid = start_game()
    if n>0:
        play_game(n, n_bombs, root, state_grid)
        root.mainloop()
