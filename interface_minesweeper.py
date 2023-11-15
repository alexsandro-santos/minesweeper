from tkinter import *
from tkinter import ttk
import random
from PIL import Image, ImageTk

colors = ['white','#bae1ff',"#baffc9","#ffffba","#ffdfba","#ffb3ba",
          "#ffb3ba","#ffb3ba","#ffb3ba","#ffb3ba"]
def open(i,j, grid):
    global root, photo, colors
    print('Opening case ',i,j)
    pressed = buttons[i][j]
    color = colors[grid[i][j]]
    new = Button(root, bg=color, fg = 'orange', width=2, height=1,
                 font = ('Arial 9 bold'), relief="sunken",
                 text=str(grid[i][j]))
    new.grid(row=i, column=j)
    buttons[i][j] = new
    new.config(state = 'disabled')
    pressed.destroy()
    

# def left_click(event): #UNUSED
#     button.config(bg="green")
#     button.config(state="disabled")

def right_click(event):
    global photo
    bot = event.widget
    if bot["bg"] == "white" and bot["text"] == "":
        event.widget.configure(bg="red")
        #event.widget.configure(image = photo)
    elif bot["bg"] == "red" and bot["text"] == "":
        event.widget.configure(text="?")
        event.widget.configure(bg="white")
    else:
        event.widget.configure(text="")

def scroll_click(event): #UNUSED
    bot = event.widget
    if bot["text"] == "" and bot["bg"] == "white":
        event.widget.configure(text="?")
    else:
        event.widget.configure(text="")
        event.widget.configure(bg="white")

def create_grid(n):
    global buttons, root, photo
    root = Tk()
    bomb = Image.open("C:/Users/eduar/Downloads/bomb.png")
    root.wm_iconphoto(False, ImageTk.PhotoImage(bomb))
    root.title("Minesweeper")
    size = int(27.5*n)
    button_size = int(size/n)
    root.geometry(str(size)+"x"+str(size))
    root.resizable(0, 0)
    #flag = Image.open("C:/Users/eduar/Downloads/tile_flag.gif")
    #photo = ImageTk.PhotoImage(flag)
    #photo = PhotoImage(file="C:/Users/eduar/Downloads/tile_flag.gif")
    grid = []
    for _ in range(n):
        grid.append([random.randint(0,5) for _ in range (n)])

    print(grid)
    print(len(grid), len(grid[0]))

    buttons = [[] for _ in range(len(grid))]

    for i in range(len(grid)):
        root.rowconfigure(i,weight=button_size)
        for j in range(len(grid[i])):
            root.columnconfigure(j,weight=button_size)
            #n=grid[i][j]
            button = Button(root, bg="white", width=2, height=1,
                            command=lambda  i=i,j=j, grid=grid: open(i,j,grid))

            #button.bind("<Button-1>", left_click)
            button.bind("<Button-2>", right_click)
            button.bind("<Button-3>", right_click)

            # Add the button to the window
            button.grid(row=i, column=j)

            # Add a reference to the button to 'buttons'
            buttons[i].append(button)

create_grid(9)
root.mainloop()

