# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 23:57:20 2018
@author: singh, davidson
"""

from tkinter import *
import tkinter.messagebox
import numpy as np
import sys 
import os

#keeps track of who's turn it is
turn=0

#bool for retry button to appear
win=False

#makes board lines
def makeBoard():
    canvas.create_line(167,0,167,500, fill = 'red')
    canvas.create_line(334,0,334,500, fill = 'red')
    canvas.create_line(0,167,500,167, fill = 'red')
    canvas.create_line(0,334,500,334, fill = 'red')
    

#update x and o's
def callback1():
    global turn
    turn +=1
    if(turn%2==0):
        b1.config(text="x")
        board[0][0]=0
    else:
        b1.config(text="o")
        board[0][0]=1
    b1.config(state=DISABLED)
    nextTurn()
    winCheck()
    
def callback2():
    global turn
    turn +=1
    if(turn%2==0):
        b2.config(text="x")
        board[0][1]=0
    else:
        b2.config(text="o")
        board[0][1]=1
    b2.config(state=DISABLED)
    nextTurn()
    winCheck()
    
def callback3():
    global turn
    turn +=1
    if(turn%2==0):
        b3.config(text="x")
        board[0][2]=0
    else:
        b3.config(text="o")
        board[0][2]=1
    b3.config(state=DISABLED)
    nextTurn()
    winCheck()
    
def callback4():
    global turn
    turn +=1
    if(turn%2==0):
        b4.config(text="x")
        board[1][0]=0
    else:
        b4.config(text="o")
        board[1][0]=1
    b4.config(state=DISABLED)
    nextTurn()
    winCheck()
    
def callback5():
    global turn
    turn +=1
    if(turn%2==0):
        b5.config(text="x")
        board[1][1]=0
    else:
        b5.config(text="o")
        board[1][1]=1
    b5.config(state=DISABLED)
    nextTurn()
    winCheck()
    
def callback6():
    global turn
    turn +=1
    if(turn%2==0):
        b6.config(text="x")
        board[1][2]=0
    else:
        b6.config(text="o")
        board[1][2]=1
    b6.config(state=DISABLED)
    nextTurn()
    winCheck()
    
def callback7():
    global turn
    turn +=1
    if(turn%2==0):
        b7.config(text="x")
        board[2][0]=0
    else:
        b7.config(text="o")
        board[2][0]=1
    b7.config(state=DISABLED)
    nextTurn()
    winCheck()
    
def callback8():
    global turn
    turn +=1
    if(turn%2==0):
        b8.config(text="x")
        board[2][1]=0
    else:
        b8.config(text="o")
        board[2][1]=1
    b8.config(state=DISABLED)
    nextTurn()
    winCheck()
    
def callback9():
    global turn
    turn +=1
    if(turn%2==0):
        b9.config(text="x")
        board[2][2]=0
    else:
        b9.config(text="o")
        board[2][2]=1
    b9.config(state=DISABLED)
    nextTurn()
    winCheck()
    
def retry():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def winCheck():
    global win
    if(board[0][0] == 0 and board[0][1] == 0 and board[0][2] == 0):
        hud.set("X wins")
        disableButtons()
        win=True
    elif(board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1):
        hud.set('O wins')
        disableButtons()
        win=True
        
    if(board[1][0] == 0 and board[1][1] == 0 and board[1][2] == 0):
        hud.set("X wins")
        disableButtons()
        win=True
    elif(board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1):
        hud.set('O wins')
        disableButtons()
        win=True
        
    if(board[2][0] == 0 and board[2][1] == 0 and board[2][2] == 0):
        hud.set("X wins")
        disableButtons()
        win=True
    elif(board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1):
        hud.set('O wins')
        disableButtons()
        win=True
        
    if(board[0][0] == 0 and board[1][0] == 0 and board[2][0] == 0):
        hud.set("X wins")
        disableButtons()
        win=True
    elif(board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1):
        hud.set('O wins')
        disableButtons()
        win=True
        
    if(board[0][1] == 0 and board[1][1] == 0 and board[2][1] == 0):
        hud.set("X wins")
        disableButtons()
        win=True
    elif(board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1):
        hud.set('O wins')
        disableButtons()
        win=True
        
    if(board[0][2] == 0 and board[1][2] == 0 and board[2][2] == 0):
        hud.set("X wins")
        disableButtons()
        win=True
    elif(board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1):
        hud.set('O wins')
        disableButtons()
        win=True
        
    if(board[0][2] == 0 and board[1][1] == 0 and board[2][0] == 0):
        hud.set("X wins")
        disableButtons()
        win=True
    elif(board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1):
        hud.set('O wins')
        disableButtons()
        win=True
        
    if(board[0][0] == 0 and board[1][1] == 0 and board[2][2] == 0):
        hud.set("X wins")
        disableButtons()
        win=True
    elif(board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1):
        hud.set('O wins')
        disableButtons()
        win=True
    
    if(win == True or turn == 9):
        if(turn == 9 and win == False):
            hud.set("tie game!")
        b10 = tkinter.Button(ttt, text="retry me daddy", command = retry,fg="black" )
        b10.pack()
        b10.place(height=50,width=100, x=200, y=200)

def nextTurn():
    global turn
    if(turn%2 == 0):
        hud.set("O's turn")
    else:
        hud.set("X's turn")

def disableButtons():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)
    
#make game board filled with non 0 and 1's
board = [[2,2,2],[2,2,2],[2,2,2]]

ttt = Tk()
ttt.title("tic tac toe")
ttt.geometry('500x500')

canvas = Canvas(ttt, width = 500, height = 500, bg = 'black')
makeBoard()

#turn/win label
hud = StringVar()
disp = Label(ttt, textvariable= hud)
disp.pack()
disp.place(height=20,width=100, x=50, y=450)
hud.set("O's turn")
    

b1 = tkinter.Button(ttt, text="click me daddy", command = callback1,fg="black" )

b1.pack()
b1.place(height=50,width=100, x=35, y=50)

b2 = tkinter.Button(ttt, text="click me daddy", command = callback2,fg="black")

b2.pack()
b2.place(height=50,width=100, x=200, y=50)

b3 = tkinter.Button(ttt, text="click me daddy", command = callback3,fg="black")

b3.pack()
b3.place(height=50,width=100, x=365, y=50)

b4 = tkinter.Button(ttt, text="click me daddy", command = callback4,fg="black")

b4.pack()
b4.place(height=50,width=100, x=35, y=225)

b5 = tkinter.Button(ttt, text="click me daddy",command = callback5,fg="black")

b5.pack()
b5.place(height=50,width=100, x=200, y=225)

b6 = tkinter.Button(ttt, text="click me daddy",command = callback6,fg="black")

b6.pack()
b6.place(height=50,width=100, x=365, y=225)

b7 = tkinter.Button(ttt, text="click me daddy",command = callback7,fg="black")

b7.pack()
b7.place(height=50,width=100, x=35, y=375)

b8 = tkinter.Button(ttt, text="click me daddy",command = callback8,fg="black")

b8.pack()
b8.place(height=50,width=100, x=200, y=375)

b9 = tkinter.Button(ttt, text="click me daddy",command = callback9,fg="black")

b9.pack()
b9.place(height=50,width=100, x=365, y=375)

canvas.pack(fill=BOTH)
ttt.mainloop()
