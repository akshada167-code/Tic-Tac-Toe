import random                 #importing all necessary liabraries
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy



def show():
    messagebox.showinfo("RULES","Rules for play game")


# sign variable to decide the turn of which player
sign = 0
 
global board                                #create an empty board 3 col,3 rows 
board = [[" " for x in range(3)] for y in range(3)]
  

 
# Check l(O/X) won the match or not
# according to the rules of the game
 
def winner(b, l):       #decide which player goes firts
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or    #creating list of string that used to pics on the board
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))#  Creates an empty board global board 
                                                                # Sets up variables for turn order sign = 0
                                                                 # Plays out each move in turn-based fashion while True:
                                                                 #Checks if there is a winner if (board[sign][0]==X
                                                               #or board[sign][1] == X) : print(You win!)break elif
                                                                #(board[sign][0] == O or board[sign][1] == O) : print(You lose!)  

#Configure text on button while playing with another player

def get_text(i, j, gb, l1, l2):             # i,j,l1,l2 there are 3 arguments these present player number 1 position in game (i     
    global sign                             # j represent player num 2
    if board[i][j] == ' ':                  # nd where they want display there position  l,r,top bottom otherwise 0 or 5 
        if sign % 2 == 0:                    #  represented by l1 and l2 represnt how many columns wide
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    if winner(board, "X"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 1 won the match")
    elif winner(board, "O"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 2 won the match")
    elif(isfull()):
        gb.destroy()
        box = messagebox.showinfo("Tie Game", "Tie Game")#its tym to play again bcz of tie

    
 # Check if the player can push the button or not

def isfree(i, j):
    return board[i][j] == " " 

# Check the board is full or not
 
def isfull():
    flag = True
    for i in board:
        if(i.count(' ') > 0):
            flag = False
    return flag 

  
# Create the GUI of game board for play along with another

def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(3):   #3
        m = 3+i
        button.append(i)  #to add
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()
 
#Decide the next move of system
 
def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner)-1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge)-1)
            return edge[move]

        
# Configure text on button while playing with system

 
def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Player won the match")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Computer won the match")
    elif(isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
    if(x):
        if sign % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0],move[1],gb,l1,l2)
 
#Create the GUI of game board for play along with system
 
def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=15, width=30)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()



 #Initialize the game board to play with system

 
def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Computer : O",
                width=10, state=DISABLED)
 
    l2.grid(row=2, column=1)
    gameboard_pc(game_board,l1,l2)

#Initialize the game board to play with another player

def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player 1 : X", width=10)
 
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Player 2 : O",
                width=10, state=DISABLED)
 
    l2.grid(row=2, column=1)
    gameboard_pl(game_board,l1,l2)



 #main function
def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Tic Tac Toe")
    wpc = partial(withpc, menu)
    wpl = partial(withplayer, menu)

     
    head = Button(menu, text="Welcome to tic-tac-toe",
                  activeforeground='red',
                  activebackground="yellow", bg="red",
                  fg="yellow", width=500, font='summer', bd=3 ,)
    
    head1 = Button(menu, text="Play Game",
                  activeforeground='red',
                  activebackground="yellow", bg="red",
                  fg="yellow", width=500, font='summer', bd=5)

    B1= Button(menu, text="Rules", command=show,
                activeforeground='light green',
                activebackground="black", bg="light green",
                fg="black", width=500, font='summer', bd=5)

    #lst=Listbox(menu,height=5)
    # list=insert(0,"fy")
     #list=insert(1,"cy")
     #list=insert(2,"by")
     #list=insert(3,"ty")
     #list=insert(4,"sy")
     #lst.place(x=100,y=200)


   

    head3 = Button(menu, text="1.Players take turns putting their marks in empty squares",
                  activeforeground='orange',
                  activebackground="white", bg="orange",
                  fg="white", width=500, font='summer', bd=5 ,)
    
    head4 = Button(menu, text="2.The game is played on a grid that's 3 squares by 3 squares",
                  activeforeground='orange',
                  activebackground="white", bg="orange",
                  fg="white", width=500, font='summer', bd=5 ,)
    
    head5 = Button(menu, text="3.you are X , your friend (or the computer in this case) is O.Players take turns putting their marks in empty squares.",
                 activeforeground='orange',
                 activebackground="white", bg="orange",
                 fg="white", width=500, font='summer', bd=5 ,)
    
    head6 = Button(menu, text="4.The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.",
                 activeforeground='orange',
                 activebackground="white", bg="orange",
                 fg="white", width=500, font='summer', bd=5 ,)
    
    head7 = Button(menu, text="5.When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.",
                  activeforeground='orange',
                  activebackground="white", bg="orange",
                  fg="white", width=500, font='summer', bd=5 ,)
    



    B2 = Button(menu, text="SINGLE PLAYER", command=wpc,
                activeforeground='light green',
                activebackground="black", bg="light green",
                fg="black", width=500, font='summer', bd=5 ,)
    
    B3 = Button(menu, text="Easy LEVEL ", command=wpc,
                activeforeground='red',
                activebackground="yellow", bg="red",
                fg="yellow", width=500, font='summer', bd=5)
    
    B4 = Button(menu, text="Mediam Level", command=wpc,
                activeforeground='red',
                activebackground="yellow", bg="red",
                fg="yellow", width=500, font='summer', bd=5)
    
    B5 = Button(menu, text="Hard Level", command=wpc,
                activeforeground='red',
                activebackground="yellow", bg="red",
                fg="yellow", width=500, font='summer', bd=5)
    
    
    B6 = Button(menu, text="MULTI PLAYER", command=wpl, activeforeground='light green',
                activebackground="yellow", bg="light green", fg="yellow",
                width=500, font='summer', bd=5)
    
    B7 = Button(menu, text="Easy Level", command=wpc,
                activeforeground='red',
                activebackground="yellow", bg="red",
                fg="yellow", width=500, font='summer', bd=5)
    
    B8 = Button(menu, text="Mediam Level", command=wpc,
                activeforeground='red',
                activebackground="yellow", bg="red",
                fg="yellow", width=500, font='summer', bd=5)
    
    
    
    B9 = Button(menu, text="Hard Level", command=wpc,
                activeforeground='red',
                activebackground="yellow", bg="red",
                fg="yellow", width=500, font='summer', bd=5)
    
    B10 = Button(menu, text="visit Again", command=menu.destroy, activeforeground='sky blue',
                activebackground="yellow", bg="sky blue", fg="yellow",
                width=500, font='summer', bd=5)



    head.pack(side='top')
    head1.pack(side='top')
    B1.pack(side='top')
    head3.pack(side='top')
    head4.pack(side='top')
    head5.pack(side='top')
    head6.pack(side='top')
    head7.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    B4.pack(side='top')
    B5.pack(side='top')
    B6.pack(side='top')
    B7.pack(side='top')
    B8.pack(side='top')
    B9.pack(side='top')
    B10.pack(side='top')

    menu.mainloop()
    

 #call main function
if __name__== '__main__':
    play()









