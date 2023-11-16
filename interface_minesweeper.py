from tkinter import *
from tkinter import ttk
import random
from PIL import Image, ImageTk
import html

flag = html.unescape('&#128681')
qm = html.unescape('&#63')

colors = ['white','#bae1ff',"#baffc9","#ffffba","#ffdfba","#ffb3ba",
          "#ffb3ba","#ffb3ba","#ffb3ba","white"]   

# def left_click(event): #UNUSED
#     button.config(bg="green")
#     button.config(state="disabled")

def right_click(event):
    global photo
    bot = event.widget
    if bot["bg"] == "light gray" and bot["text"] == "":
        event.widget.configure(bg="red")
        event.widget.configure(text = flag)
    elif bot["text"] == flag:
        event.widget.configure(text=qm)
        event.widget.configure(bg="light blue")
    else:
        event.widget.configure(text="")
        event.widget.configure(bg="light gray")

def scroll_click(event): #UNUSED
    bot = event.widget
    if bot["text"] == "" and bot["bg"] == "white":
        event.widget.configure(text="?")
    else:
        event.widget.configure(text="")
        event.widget.configure(bg="white")

bomb = html.unescape('&#128163')

def get_text(grid, i, j):
    global bomb
    nb = grid[i][j]
    if nb == -1:
        return bomb
    elif nb == 0:
        return ''
    else:
        return str(nb)
    
def create_grid(grid):
    global buttons, root, photo
    n = len(grid)
    root = Tk()
    bomb = Image.open("C:/Users/eduar/Downloads/bomb.png")
    root.wm_iconphoto(False, ImageTk.PhotoImage(bomb))
    root.title("Minesweeper")
    size = int(27.5*n)
    button_size = int(size/n)
    root.geometry(str(size)+"x"+str(size))
    root.resizable(0, 0)

    buttons = [[] for _ in range(len(grid))]

    for i in range(len(grid)):
        root.rowconfigure(i,weight=button_size)
        for j in range(len(grid[i])):
            root.columnconfigure(j,weight=button_size)
            button = Button(root, bg="light gray", width=2, height=1,
                            font = ('Helvetica 9 bold'),
                            command=lambda  i=i,j=j, grid=grid: open(i,j,grid))

            #button.bind("<Button-1>", left_click)
            button.bind("<Button-2>", right_click)
            button.bind("<Button-3>", right_click)
            button.grid(row=i, column=j)
            buttons[i].append(button)

def open(i,j, grid):
    global root, colors
    print('Opening case ',i,j)
    pressed = buttons[i][j]
    color = colors[grid[i][j]]
    text = get_text(grid,i,j)
    new = Button(root, bg=color, fg = 'orange', width=2, height=1,
                 font = ('Arial 9 bold'), relief="sunken",
                 text=text)
    new.grid(row=i, column=j)
    buttons[i][j] = new
    new.config(state = 'disabled')
    pressed.destroy()

x=5
grid = []
for _ in range(x):
    grid.append([random.choice([-1,0,0,0,0,0]) for _ in range (x)])
    
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == -1:
            try:
                grid[i][j-1] += 1
            except: pass
            try:
                grid[i][j+1] += 1
            except: pass
            try:
                grid[i-1][j-1] += 1
            except: pass
            try:
                grid[i-1][j] += 1
            except: pass
            try:
                grid[i-1][j+1] += 1
            except: pass
            try:
                grid[i+1][j-1] += 1
            except: pass
            try:
                grid[i+1][j] += 1
            except: pass
            try:
                grid[i+1][j+1] += 1
            except: pass

print(grid)
print(len(grid), len(grid[0]))

create_grid(grid)
root.mainloop()

