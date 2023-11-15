from tkinter import *
from tkinter import ttk
import random



def open(i,j, grid):
    global root
    print('Opening case ',i,j)
    pressed = buttons[i][j]
    new = Button(root, bg="white", fg = 'orange', width=2, height=1,
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
    bot = event.widget
    if bot["bg"] == "white" and bot["text"] == "":
        event.widget.configure(bg="red")
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
    global buttons, root
    root = Tk()
    root.title("Minesweeper")
    size = int(27.5*n)
    button_size = int(size/10)
    root.geometry(str(size)+"x"+str(size))
    root.resizable(0, 0)
    grid = []
    for _ in range(n):
        grid.append([random.choice([0,1,2,3,'X']) for _ in range (n)])

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

create_grid(10)
root.mainloop()
''''button = Button(root, bg="White", width=5, height=1)
button.grid(row=11, column=11)
button2 = Button(root, bg="Gray", width=5, height=1)
button2.grid(row=10, column=10)
button3 = Button(root, bg="Orange", width=5, height=1)
button3.grid(row=10, column=10)'''

