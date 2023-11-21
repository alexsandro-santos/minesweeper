# Product

Minesweeper game implemented via Python with a graphical interface created with Tkinter.

## How to play

1. Clone our repository, that is, download the files of our game. For that, open a terminal and type the following command.
```
git clone https://gitlab-cw1.centralesupelec.fr/eppa-python/minesweeper.git
```
2. Enter the folder of the repository with the following command.
```
cd minesweeper
```
3. Execute the game with one of the following commands depending on your operating system.
```
python main.py
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; or
```
python3 main.py
```
3. A screen should open and then you can start playing.

## Features

- Difficulty choice;
- Random bomb positioning;
- First click is never a bomb;
- Intuitive Graphical interface which allows for clicking, using flags, using '?', creating new game;
- Game code and interface code separated in packages;
- Modular approach, with functions executing one task only.

## Beauty and ease to play

- Interface with retro design, similar to many existing minesweeper games;
- Bombs, flags and '?' with nice images;
- Smile button to create a new game;
- Choice of difficulty between easy, medium or hard.

## TDD and First week increments

For this project, it was not only possible to adapt the same Test Driven Developpement approach to a new system, but it was also possible to reuse some functions that our group implemented for 2048.

### Test driven developpement:

 [Here](https://gitlab-cw1.centralesupelec.fr/eppa-python/minesweeper/-/blob/alexsandro/test_grid.py?ref_type=heads) we implemented tests that our created functions should pass, and as we already knew, the effectiveness of this approach helped us not only to encounter less code problems, but also minimized their impact. 

 Appart from that, some exemples of functions created for the first week that were reused are shown below:

```
def get_all_tiles(grid):
    tiles = [item for row in grid for item in row]
    return tiles
```
```
def grid_to_string(grid):
    max_tile = 2
    tile_sep = '='*(max_tile + 2)
    line_sep = '\n '+' '.join(tile_sep for _ in grid[0])+' \n'
    grid_str = ''
    for line in grid:
        grid_str += line_sep
        line = [tile if tile != -1 else '*' for tile in line]
        grid_str += '|'+'|'.join(str(tile).center(max_tile+2) for tile in line)+'|'
    grid_str += line_sep

    return grid_str
```

## Packages and functions

To create a very simple and understandable code, and also to minimize the amount of problems encountered during developpement, we opted for separating the game package and the interface package. As expected, in the main function, it was necessary to import the game and the interface. 

```
from game_minesweeper.grid_minesweeper import *
from game_minesweeper.textual_minesweeper import *
```

As for the use of functions, the group had a rule that one function implemented one and one only task. This makes error finding very easy and the code is extremely easy to read, so replicating our code in another machine would be simple. In total, 23 functions were implemented.

***

## Team work

In order to optimize time consumption and to create better and more specific functions, we separated three zones of work. As in a usual team-work environment, all members participated actively in all areas, some programming more in their zone while others would validate the progress or give new helpful ideas. 

We also worked every single shift together, and it was great. The benefits were not only felt in the developpement of the game, where new ideas would show up to help us advance, but also in our personal links to one another. Working together demanded a lot of respect for different ideas and care on how to expose conflicting ideas without issues. 

### Game developpement
Team members Pedro and Alexsandro were in charge of developping the game.

### Interface developpement
Team member Eduardo was the main responsible for the creation of the graphical interface via Tkinter, receiving help from Team member Alexsandro for the game-interface integration.

### Tests creation
Team member Paola was responsible for the creation of all tests which our functions had to pass in order to verify that all outputs were as imagined. Team member Pedro helped.
