from tkinter import *
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import html

#diff = 0

flag = html.unescape('&#128681')
qm = html.unescape('&#63')
bomb = html.unescape('&#128163')
exploded = html.unescape('&#128165')
smile = html.unescape("&#128578")
sad = html.unescape("&#128531")
winface = html.unescape("&#128526")
colors = {" ":"white",1:"#bae1ff",2:"#baffc9",3:"#ffffba",4:"#ffdfba",5:"#ffb3ba",
          6:"#ffb3ba",7:"#ffb3ba",8:"#ffb3ba",-1:"white"} 

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
    bot = event.widget
    if bot['state'] == 'normal':
        if bot["bg"] == "gray" and bot["text"] == "":
            bot.configure(bg="red")
            bot.configure(text = flag)
        elif bot["text"] == flag:
            bot.configure(text=qm)
            bot.configure(bg="light blue")
        else:
            bot.configure(text="")
            bot.configure(bg="gray")

def left_click_startup(event):
    global diff
    bot = event.widget
    diff = bot['text'].lower()

def get_updated_value(event):
    global diff
    print(diff)

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
    global diff
    root = Tk()
    diff = StringVar()
    icon = Image.open("C:/Users/eduar/Downloads/bomb.png")
    root.wm_iconphoto(True, ImageTk.PhotoImage(icon))
    root.title("Minesweeper")
    root.resizable(0, 0)
    Label(root, text='Welcome to', font= ('Helvetica 20 bold')).grid(row=0,column=0)
    Label(root, text=bomb+'Minesweeper'+bomb, font= ('Helvetica 20 bold')).grid(row=1,column=0)
    Label(root, text='Select your difficulty:', font= ('Helvetica 12 underline')).grid(row=2,column=0)
    Label(root).grid(row=3,column=0)
    Button(root, text='Easy', font= ('Helvetica 20'), width=8, height=1,
           command= lambda string = 'easy': diff.set(string)).grid(row=4,column=0) # vai chamar a função pra criar o jogo
    Label(root, text='10x10 grid, 20 bombs', font= ('Helvetica 12')).grid(row=5,column=0)
    Label(root).grid(row=6,column=0)
    Button(root, text='Medium', font= ('Helvetica 20'), width=8, height=1,
           command=lambda string = 'medium': diff.set(string)).grid(row=7,column=0)
    Label(root, text='16x16 grid, 35 bombs', font= ('Helvetica 12')).grid(row=8,column=0)
    Label(root).grid(row=9,column=0)
    Button(root, text='Hard', font= ('Helvetica 20'), width=8, height=1,
                command=lambda string = 'hard': diff.set(string)).grid(row=10,column=0)
    Label(root, text='20x20 grid, 50 bombs', font= ('Helvetica 12')).grid(row=11,column=0)
    Label(root).grid(row=12,column=0)
    root.protocol("WM_DELETE_WINDOW", lambda arg=root: on_closing(arg))
    return root

def change(l1, diff):
    l1['text']=diff

def press_button(string):
    global diff
    diff = string
    #print(diff)


def on_closing(root):
    global game_over,x,y
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        game_over = True
        x=0
        y=0



def read_click(m,n):
    global x,y
    x.set(m)
    y.set(n)


def create_grid_gui(root, grid, start_function): #will receive the state_grid generated by the game code
    global  buttons, mainFrame, bomb, smile, rb, x,y
    x,y = IntVar(), IntVar()
    root.withdraw()
    try: mainFrame.destroy()
    except: pass

    #grid = setup_grid(n) #será substituido pelo criador do jogo
    mainFrame = Toplevel()
    mainFrame.title("Minesweeper")
    n = len(grid)
    button_size = 25
    mainFrame.resizable(0, 0)

    l1= Label(mainFrame, text=bomb+'Minesweeper'+bomb, font= ('Helvetica 20 underline'))
    l1.grid(column=0,row=0, columnspan=n+2,sticky=N+E+S+W)
    rb = Button(mainFrame, text=smile,font= ('Arial 12 bold'),
                command=start_function, bg='yellow') #, fg='yellow')
    rb.grid(column=int(n/2)+1,row=1,columnspan=2)#,sticky='NEWS')
    buttons = [[] for _ in range(len(grid))]
    for i in range(len(grid)+2):
        mainFrame.rowconfigure(i,weight=button_size)
        mainFrame.columnconfigure(i,weight=button_size)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            button = Button(mainFrame, bg="gray", width=2, height=1,
                            font = ('Helvetica 9 bold'),
                            command=lambda  m=i,n=j: read_click(m,n))
            button.bind("<Button-2>", right_click)
            button.bind("<Button-3>", right_click)
            button.grid(row=i+2, column=j+2)
            buttons[i].append(button)
    #mainFrame.protocol("WM_DELETE_WINDOW", )
    mainFrame.protocol("WM_DELETE_WINDOW", lambda arg=root: on_closing(arg))
    
def open_button(i,j, state_grid,game_grid, text = ' '):
    global mainFrame, colors, bomb, exploded, rb, sad, winface
    #print('Opening case ',i,j)
    pressed = buttons[i][j]
    if pressed['state'] != 'disabled':
        color = colors.get(state_grid[i][j],"white")
        if text == ' ':
            text = get_text(state_grid,i,j)
        new = Button(mainFrame, bg=color, fg = 'orange', width=2, height=1, ##fg orange ?
                    font = ('Arial 9 bold'), relief="sunken",
                    text=text)
        new.grid(row=i+2, column=j+2)
        buttons[i][j] = new
        new['state'] = 'disabled'
        pressed.destroy()
        if text == exploded:
            show_bombs(state_grid, game_grid)
    
def show_bombs(state_grid, game_grid):
    rb['text']=sad
    for i in range(len(state_grid)):
        for j in range(len(state_grid)):
            print('analyzing', i,j)
            if game_grid[i][j] == -1 and buttons[i][j]['text'] != exploded:
                open_button(i,j,state_grid,game_grid,bomb)
                print('bomb at', i,j)
            else:
                buttons[i][j]['state'] = 'disabled'
                print('disabling', i,j)

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

running = True

if __name__ == "__main__":
    root = startup()
    #root.mainloop()
    while running:
        root.update()
    