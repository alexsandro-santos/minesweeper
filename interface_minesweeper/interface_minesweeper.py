from tkinter import *
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import html


flag = html.unescape('&#128681')
qm = html.unescape('&#63')
bomb = html.unescape('&#128163')
exploded = html.unescape('&#128165')
smile = html.unescape("&#128578")
sad = html.unescape("&#128531")
winface = html.unescape("&#128526")
colors = ['white','#bae1ff',"#baffc9","#ffffba","#ffdfba","#ffb3ba",
          "#ffb3ba","#ffb3ba","#ffb3ba","white"]   

# def left_click(event): #UNUSED
#     button.config(bg="green")
#     button.config(state="disabled")

# def scroll_click(event): #UNUSED
#     bot = event.widget
#     if bot["text"] == "" and bot["bg"] == "white":
#         event.widget.configure(text="?")
#     else:
#         event.widget.configure(text="")
#         event.widget.configure(bg="white")

def right_click(event):
    global photo
    bot = event.widget
    if bot['state'] == 'normal':
        if bot["bg"] == "light gray" and bot["text"] == "":
            bot.configure(bg="red")
            bot.configure(text = flag)
        elif bot["text"] == flag:
            bot.configure(text=qm)
            bot.configure(bg="light blue")
        else:
            bot.configure(text="")
            bot.configure(bg="light gray")

def get_text(grid, i, j):
    global exploded
    nb = grid[i][j]
    if nb == -1:
        return exploded
    elif nb == 0:
        return ''
    else:
        return str(nb)

def startup():
    global root
    root = Tk()
    icon = Image.open("C:/Users/eduar/Downloads/bomb.png")
    root.wm_iconphoto(True, ImageTk.PhotoImage(icon))
    root.title("Minesweeper")
    root.resizable(0, 0)
    Label(root, text='Welcome to', font= ('Helvetica 20 bold')).grid(row=0,column=0)
    Label(root, text=bomb+'Minesweeper'+bomb, font= ('Helvetica 20 bold')).grid(row=1,column=0)
    Label(root, text='Select your difficulty:', font= ('Helvetica 12 underline')).grid(row=2,column=0)
    Label(root).grid(row=3,column=0)
    Button(root, text='Easy', font= ('Helvetica 20'), width=8, height=1,
           command=lambda n=10: create_grid(n)).grid(row=4,column=0) # vai chamar a função pra criar o jogo
    Label(root, text='10x10 grid, 20 bombs', font= ('Helvetica 12')).grid(row=5,column=0)
    Label(root).grid(row=6,column=0)
    Button(root, text='Medium', font= ('Helvetica 20'), width=8, height=1,
           command=lambda n=16: create_grid(n)).grid(row=7,column=0)
    Label(root, text='16x16 grid, 35 bombs', font= ('Helvetica 12')).grid(row=8,column=0)
    Label(root).grid(row=9,column=0)
    Button(root, text='Hard', font= ('Helvetica 20'), width=8, height=1,
           command=lambda n=20: create_grid(n)).grid(row=10,column=0)
    Label(root, text='20x20 grid, 50 bombs', font= ('Helvetica 12')).grid(row=11,column=0)
    Label(root).grid(row=12,column=0)

def on_closing():
    global root
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


def create_grid(n): #will receive the state_grid generated by the game code
                    
    global root, buttons, mainFrame, bomb, smile, mainFrame, rb
    root.withdraw()
    try: mainFrame.destroy()
    except: pass

    grid = setup_grid(n) #será substituido pelo criador do jogo
    mainFrame = Toplevel()
    mainFrame.title("Minesweeper")
    n = len(grid)
    button_size = 25
    mainFrame.resizable(0, 0)

    l1= Label(mainFrame, text=bomb+'Minesweeper'+bomb, font= ('Helvetica 20 underline'))
    l1.grid(column=0,row=0, columnspan=n+2,sticky=N+E+S+W)
    rb = Button(mainFrame, text=smile,font= ('Arial 12 bold'),
                command=lambda n = n: create_grid(n), bg='yellow') #, fg='yellow')
    rb.grid(column=int(n/2)+1,row=1,columnspan=2)#,sticky='NEWS')
    buttons = [[] for _ in range(len(grid))]
    for i in range(len(grid)+2):
        mainFrame.rowconfigure(i,weight=button_size)
        mainFrame.columnconfigure(i,weight=button_size)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            button = Button(mainFrame, bg="light gray", width=2, height=1,
                            font = ('Helvetica 9 bold'),
                            command=lambda  i=i,j=j, grid=grid: open(i,j,grid))
            button.bind("<Button-2>", right_click)
            button.bind("<Button-3>", right_click)
            button.grid(row=i+2, column=j+2)
            buttons[i].append(button)
    mainFrame.protocol("WM_DELETE_WINDOW", on_closing)
    
def open(i,j, grid, text = ''):
    global mainFrame, colors, bomb, exploded, rb, sad, winface
    #print('Opening case ',i,j)
    pressed = buttons[i][j]
    color = colors[grid[i][j]]
    if text == '':
        text = get_text(grid,i,j)
    new = Button(mainFrame, bg=color, fg = 'orange', width=2, height=1, ##fg orange ?
                 font = ('Arial 9 bold'), relief="sunken",
                 text=text)
    new.grid(row=i+2, column=j+2)
    buttons[i][j] = new
    new['state'] = 'disabled'
    pressed.destroy()
    if text == exploded:
        rb['text']=sad
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == -1 and buttons[i][j]['text'] != exploded:
                    open(i,j,grid,bomb)
                else:
                    buttons[i][j]['state'] = 'disabled'

def setup_grid(x):
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

    #print(grid)
    #print(len(grid), len(grid[0]))
    return grid

if __name__ == "__main__":
    startup()
    root.mainloop()