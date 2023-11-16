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

# def startup():
# Seria interessante mover a criação da root pra cá
# Na root selecionaria a dificuldade e chamaria a função
# responsável por criar o mainframe (e o jogo)

def create_grid(grid):
    global buttons, mainFrame, bomb
    n = len(grid)
    root = Tk()
    mainFrame = Toplevel()
    icon = Image.open("C:/Users/eduar/Downloads/bomb.png")
    root.wm_iconphoto(True, ImageTk.PhotoImage(icon))
    root.title("Minesweeper")
    mainFrame.title("Minesweeper")
    size = int(24*n)
    button_size = int(size/n)
    mainFrame.geometry(str(size)+"x"+str(size))
    mainFrame.resizable(0, 0)
    text_size = 20
    l1= Label(mainFrame, text=bomb+'Minesweeper'+bomb, font= ('Helvetica'+str(text_size)+'underline'))
    l1.grid(column=1,row=0, columnspan=n+2,sticky=N+E+S+W)
    buttons = [[] for _ in range(len(grid))]

    for i in range(len(grid)):
        mainFrame.rowconfigure(i+2,weight=button_size)
        for j in range(len(grid[i])):
            #mainFrame.rowconfigure(i+2,weight=button_size+5)
            #mainFrame.columnconfigure(j+2,weight=button_size)
            button = Button(mainFrame, bg="light gray", width=2, height=1,
                            font = ('Helvetica 9 bold'),
                            command=lambda  i=i,j=j, grid=grid: open(i,j,grid))

            #button.bind("<Button-1>", left_click)
            button.bind("<Button-2>", right_click)
            button.bind("<Button-3>", right_click)
            button.grid(row=i+2, column=j+2)
            buttons[i].append(button)

def open(i,j, grid):
    global mainFrame, colors
    print('Opening case ',i,j)
    pressed = buttons[i][j]
    color = colors[grid[i][j]]
    text = get_text(grid,i,j)
    new = Button(mainFrame, bg=color, fg = 'orange', width=2, height=1,
                 font = ('Arial 9 bold'), relief="sunken",
                 text=text)
    new.grid(row=i+2, column=j+2)
    buttons[i][j] = new
    new.config(state = 'disabled')
    pressed.destroy()

x=20
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
mainFrame.mainloop()

