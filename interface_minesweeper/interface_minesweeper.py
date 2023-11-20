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

def read_click(m,n):
    global x,y,cmd
    x.set(m)
    y.set(n)
    cmd.set('o')

def right_click(event,m,n):
    global bomb_count, label_count, cmd, x, y
    bot = event.widget
    x.set(m)
    y.set(n)
    if bot['state'] == 'normal':
        if bot["text"] == " ":
            bot.configure(bg="red")
            bot.configure(text = flag)
            cmd.set('f')
            if bomb_count.get() > 0:
                bomb_count.set(bomb_count.get()-1)
                label_count['text'] = bomb_count.get()
        elif bot["text"] == flag:
            bot.configure(text=qm)
            bot.configure(bg="light blue")
            bomb_count.set(bomb_count.get()+1)
            label_count['text'] = bomb_count.get()
            cmd.set('f')
        elif bot["text"] == qm:
            bot.configure(text=" ")
            bot.configure(bg="gray")
            cmd.set('f')


# def right_click(event):
#     global bomb_count, label_count, cmd, x, y
#     cmd = StringVar()
#     bot = event.widget
#     if bot['state'] == 'normal':
#         if bot["bg"] == "gray" and bot["text"] == "":
#             bot.configure(bg="red")
#             bot.configure(text = flag)
#             cmd.set('f')
#             if bomb_count.get() > 0:
#                 bomb_count.set(bomb_count.get()-1)
#                 label_count['text'] = bomb_count.get()
#         elif bot["text"] == flag:
#             bot.configure(text=qm)
#             bot.configure(bg="light blue")
#             bomb_count.set(bomb_count.get()+1)
#             label_count['text'] = bomb_count.get()
#         else:
#             bot.configure(text="")
#             bot.configure(bg="gray")
#             bot.configure(state = 'normal')

def left_click_startup(event):
    global diff
    bot = event.widget
    diff = bot['text'].lower()

def get_text(grid, i, j):
    global exploded
    nb = grid[i][j]
    if nb == -1:
        return exploded
    elif nb == 0:
        return " "
    elif nb in range(9):
        return str(nb)
    else:
        return " "

def startup():
    global diff
    root = Tk()
    diff = StringVar()
    icon = Image.open("minesweeper/bomb.png")
    root.wm_iconphoto(True, ImageTk.PhotoImage(icon))
    root.title("Minesweeper")
    root.resizable(0, 0)
    Label(root, text='Welcome to', font= ('Helvetica 20 bold')).grid(row=0,column=0)
    Label(root, text=bomb+'Minesweeper'+bomb, font= ('Helvetica 20 bold')).grid(row=1,column=0)
    Label(root, text='Select your difficulty:', font= ('Helvetica 12 underline')).grid(row=2,column=0)
    Label(root).grid(row=3,column=0)
    Button(root, text='Easy', font= ('Helvetica 20'), width=8, height=1,
           command= lambda string = 'easy': diff.set(string)).grid(row=4,column=0) # vai chamar a função pra criar o jogo
    Label(root, text='10x10 grid, 10 bombs', font= ('Helvetica 12')).grid(row=5,column=0)
    Label(root).grid(row=6,column=0)
    Button(root, text='Medium', font= ('Helvetica 20'), width=8, height=1,
           command=lambda string = 'medium': diff.set(string)).grid(row=7,column=0)
    Label(root, text='16x16 grid, 35 bombs', font= ('Helvetica 12')).grid(row=8,column=0)
    Label(root).grid(row=9,column=0)
    Button(root, text='Hard', font= ('Helvetica 20'), width=8, height=1,
                command=lambda string = 'hard': diff.set(string)).grid(row=10,column=0)
    Label(root, text='20x20 grid, 80 bombs', font= ('Helvetica 12')).grid(row=11,column=0)
    Label(root).grid(row=12,column=0)
    root.protocol("WM_DELETE_WINDOW", lambda arg=root: on_closing(arg))

    root.update_idletasks()

    w = root.winfo_width() # width for the Tk root
    h = root.winfo_height() # height for the Tk root

    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    window_x = (ws/2) - (w/2)
    window_y = (hs/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, window_x, window_y))

    return root


def on_closing(root):
    global x, diff, window_open
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        try:
            diff.set('close')
            x.set(-1)
            window_open = False
            #root.quit()
            root.destroy()
            print('root destruído')
        except: pass
        
def reset_game(restart_function):
    global x, diff, window_open
    try:
        diff.set('close')
        x.set(-1)
        window_open = False
        restart_function()
        print('Jogo reiniciado')
        
    except: pass
        



def create_grid_gui(root, grid, start_function): #will receive the state_grid generated by the game code
    global  buttons, mainFrame, bomb, smile, rb, x,y
    global bomb_count, label_count, cmd

    x,y = IntVar(), IntVar()
    cmd = StringVar()
    root.withdraw()

    try: mainFrame.destroy()
    except: print("No mainFrame to destroy")

    #grid = setup_grid(n) #será substituido pelo criador do jogo
    mainFrame = Toplevel()
    mainFrame.title("Minesweeper")
    n = len(grid)
    bomb_count = IntVar()
    if n == 10:
        bomb_count.set(10)
    elif n==16:
        bomb_count.set(35)
    else:
        bomb_count.set(80)
    button_size = 25
    mainFrame.resizable(0, 0)

    l1= Label(mainFrame, text=bomb+'Minesweeper'+bomb, font= ('Helvetica 20 underline'))
    l1.grid(column=0,row=0, columnspan=n+2,sticky=N+E+S+W)
    # rb = Button(mainFrame, text=smile,font= ('Arial 12 bold'),
    #             command=start_function, bg='yellow')
    rb = Button(mainFrame, text=smile,font= ('Arial 12 bold'),
                command=lambda x=start_function: reset_game(x), bg='yellow') #, fg='yellow')
    rb.grid(column=int(n/2)+1,row=1,columnspan=2)#,sticky='NEWS')
    l2= Label(mainFrame, text = 'Bombs:', font= ('Helvetica 10'))
    l2.grid(column = n-2, row = 1, columnspan=4)
    label_count= Label(mainFrame, text = bomb_count.get(), font= ('Helvetica 10'))
    label_count.grid(column = n+1, row = 1, columnspan=1)
    buttons = [[] for _ in range(len(grid))]
    for i in range(len(grid)+2):
        mainFrame.rowconfigure(i,weight=button_size)
        mainFrame.columnconfigure(i,weight=button_size)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            button = Button(mainFrame, bg="gray", width=2, height=1,
                            font = ('Helvetica 9 bold'), text= " ",
                            command=lambda  m=i,n=j: read_click(m,n))
            button.bind("<Button-2>", lambda event,m=i, n=j: right_click(event,m,n))
            button.bind("<Button-3>", lambda event,m=i, n=j: right_click(event,m,n))
            button.grid(row=i+2, column=j+2)
            buttons[i].append(button)
    #mainFrame.protocol("WM_DELETE_WINDOW", )
    mainFrame.protocol("WM_DELETE_WINDOW", lambda arg=root: on_closing(arg))

    mainFrame.update_idletasks()

    w = mainFrame.winfo_width() # width for the Tk root
    h = mainFrame.winfo_height() # height for the Tk root

    ws = mainFrame.winfo_screenwidth() # width of the screen
    hs = mainFrame.winfo_screenheight() # height of the screen

    window_x = (ws/2) - (w/2)
    window_y = (hs/2) - (h/2)

    mainFrame.geometry('%dx%d+%d+%d' % (w, h, window_x, window_y))

    return mainFrame
    
def open_button(i,j,command, state_grid,game_grid, text = ' '):
    global mainFrame, colors, bomb, exploded, rb, sad, winface
    #print('Opening case ',i,j)
    pressed = buttons[i][j]
    if text == ' ':
        text = get_text(state_grid,i,j)
    if pressed['state'] != 'disabled' and command == 'o':
        # if pressed['text'] not in (qm, flag):
        color = colors.get(state_grid[i][j],"white")
        new = Button(mainFrame, bg=color, fg = 'orange', width=2, height=1,
                    font = ('Arial 9 bold'), relief="sunken",
                    text=text)
        new.grid(row=i+2, column=j+2)
        buttons[i][j] = new
        new['state'] = 'disabled'
        pressed.destroy()
        if text == exploded:
            show_bombs(state_grid, game_grid)
    #elif pressed['state'] != 'disabled' and cmd == 'f':

    
def show_bombs(state_grid, game_grid):
    rb['text']=sad
    for i in range(len(state_grid)):
        for j in range(len(state_grid)):
            #print('analyzing', i,j)
            if game_grid[i][j] == -1 and buttons[i][j]['text'] != exploded:
                open_button(i,j,'o',state_grid,game_grid,bomb)
                #print('bomb at', i,j)
            else:
                buttons[i][j]['state'] = 'disabled'
                #print('disabling', i,j)

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

# if __name__ == "__main__":
#     root = startup()
#     #root.mainloop()
#     while running:
#         root.update()
    