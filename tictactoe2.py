# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 11:18:52 2018

@author: singh
"""

from tkinter import *
import tkinter.messagebox
import numpy as np
import sys 
import os

class Board:
    
    #keeps track of who's turn it is
    global turn
    turn=0

    #bool for retry button to appear
    global win
    win=False
    
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    
    def makeBoard(self):
        canvas.create_line(167,0,167,500, fill = 'red')
        canvas.create_line(334,0,334,500, fill = 'red')
        canvas.create_line(0,167,500,167, fill = 'red')
        canvas.create_line(0,334,500,334, fill = 'red')
        

    #update x and o's for each individual button
    def callback1(self):
        global turn
        turn +=1
        if(turn%2==0):
            b1.config(text="x")
            board[0][0]=0
        else:
            b1.config(text="o")
            board[0][0]=1
        b1.config(state=DISABLED)
        self.nextTurn()
        self.winCheck()
        
    def callback2(self):
        global turn
        turn +=1
        if(turn%2==0):
            b2.config(text="x")
            board[0][1]=0
        else:
            b2.config(text="o")
            board[0][1]=1
        b2.config(state=DISABLED)
        self.nextTurn()
        self.winCheck()
        
    def callback3(self):
        global turn
        turn +=1
        if(turn%2==0):
            b3.config(text="x")
            board[0][2]=0
        else:
            b3.config(text="o")
            board[0][2]=1
        b3.config(state=DISABLED)
        self.nextTurn()
        self.winCheck()
        
    def callback4(self):
        global turn
        turn +=1
        if(turn%2==0):
            b4.config(text="x")
            board[1][0]=0
        else:
            b4.config(text="o")
            board[1][0]=1
        b4.config(state=DISABLED)
        self.nextTurn()
        self.winCheck()
        
    def callback5(self):
        global turn
        turn +=1
        if(turn%2==0):
            b5.config(text="x")
            board[1][1]=0
        else:
            b5.config(text="o")
            board[1][1]=1
        b5.config(state=DISABLED)
        self.nextTurn()
        self.winCheck()
        
    def callback6(self):
        global turn
        turn +=1
        if(turn%2==0):
            b6.config(text="x")
            board[1][2]=0
        else:
            b6.config(text="o")
            board[1][2]=1
        b6.config(state=DISABLED)
        self.nextTurn()
        self.winCheck()
        
    def callback7(self):
        global turn
        turn +=1
        if(turn%2==0):
            b7.config(text="x")
            board[2][0]=0
        else:
            b7.config(text="o")
            board[2][0]=1
        b7.config(state=DISABLED)
        self.nextTurn()
        self.winCheck()
        
    def callback8(self):
        global turn
        turn +=1
        if(turn%2==0):
            b8.config(text="x")
            board[2][1]=0
        else:
            b8.config(text="o")
            board[2][1]=1
        b8.config(state=DISABLED)
        self.nextTurn()
        self.winCheck()
        
    def callback9(self):
        global turn
        turn +=1
        if(turn%2==0):
            b9.config(text="x")
            board[2][2]=0
        else:
            b9.config(text="o")
            board[2][2]=1
        b9.config(state=DISABLED)
        self.nextTurn()
        self.winCheck()
      
    #starts game over if clicked 
    def retry(self):
        python = sys.executable
        os.execl(python, python, * sys.argv)
        
    #logic for checking who wins
    def winCheck(self):
        global win
        if(board[0][0] == 0 and board[0][1] == 0 and board[0][2] == 0):
            hud.set("X wins")
            self.disableButtons()
            win=True
        elif(board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1):
            hud.set('O wins')
            self.disableButtons()
            win=True
            
        if(board[1][0] == 0 and board[1][1] == 0 and board[1][2] == 0):
            hud.set("X wins")
            self.disableButtons()
            win=True
        elif(board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1):
            hud.set('O wins')
            self.disableButtons()
            win=True
            
        if(board[2][0] == 0 and board[2][1] == 0 and board[2][2] == 0):
            hud.set("X wins")
            self.disableButtons()
            win=True
        elif(board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1):
            hud.set('O wins')
            self.disableButtons()
            win=True
            
        if(board[0][0] == 0 and board[1][0] == 0 and board[2][0] == 0):
            hud.set("X wins")
            self.disableButtons()
            win=True
        elif(board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1):
            hud.set('O wins')
            self.disableButtons()
            win=True
            
        if(board[0][1] == 0 and board[1][1] == 0 and board[2][1] == 0):
            hud.set("X wins")
            self.disableButtons()
            win=True
        elif(board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1):
            hud.set('O wins')
            self.disableButtons()
            win=True
            
        if(board[0][2] == 0 and board[1][2] == 0 and board[2][2] == 0):
            hud.set("X wins")
            self.disableButtons()
            win=True
        elif(board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1):
            hud.set('O wins')
            self.disableButtons()
            win=True
            
        if(board[0][2] == 0 and board[1][1] == 0 and board[2][0] == 0):
            hud.set("X wins")
            self.disableButtons()
            win=True
        elif(board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1):
            hud.set('O wins')
            self.disableButtons()
            win=True
            
        if(board[0][0] == 0 and board[1][1] == 0 and board[2][2] == 0):
            hud.set("X wins")
            self.disableButtons()
            win=True
        elif(board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1):
            hud.set('O wins')
            self.disableButtons()
            win=True
        
        if(win == True or turn == 9):
            if(turn == 9 and win == False):
                hud.set("tie game!")
            b10 = tkinter.Button(ttt, text="retry", command = self.retry,fg="black" )
            b10.pack()
            b10.place(height=50,width=100, x=200, y=200)

    #turn updater
    def nextTurn(self):
        global turn
        if(turn%2 == 0):
            hud.set("O's turn")
        else:
            hud.set("X's turn")
            
    #disables all buttons, called if game is won
    def disableButtons(self):
        b1.config(state = DISABLED)
        b2.config(state = DISABLED)
        b3.config(state = DISABLED)
        b4.config(state = DISABLED)
        b5.config(state = DISABLED)
        b6.config(state = DISABLED)
        b7.config(state = DISABLED)
        b8.config(state = DISABLED)
        b9.config(state = DISABLED)
 

#creating board
global board
board = [[2,2,2],[2,2,2],[2,2,2]]
global ttt
ttt = Tk()
ttt.title("tic tac toe")
ttt.geometry('500x500')
canvas = Canvas(ttt, width = 500, height = 500, bg = 'black')
    #turn/win label
global hud 
hud = StringVar()
global disp 
disp = Label(ttt, textvariable= hud)
disp.pack()
disp.place(height=20,width=100, x=50, y=450)
hud.set("O's turn")
boardGame = Board()
#intializing buttons on the board
b1 = tkinter.Button(ttt, text="click", command = boardGame.callback1,fg="black" )
        
b1.pack()
b1.place(height=50,width=100, x=35, y=50)
        
b2 = tkinter.Button(ttt, text="click", command = boardGame.callback2,fg="black")
        
b2.pack()
b2.place(height=50,width=100, x=200, y=50)
        
b3 = tkinter.Button(ttt, text="click", command = boardGame.callback3,fg="black")
        
b3.pack()
b3.place(height=50,width=100, x=365, y=50)
        
b4 = tkinter.Button(ttt, text="click", command = boardGame.callback4,fg="black")
        
b4.pack()
b4.place(height=50,width=100, x=35, y=225)
        
b5 = tkinter.Button(ttt, text="click",command = boardGame.callback5,fg="black")
        
b5.pack()
b5.place(height=50,width=100, x=200, y=225)
        
b6 = tkinter.Button(ttt, text="click",command = boardGame.callback6,fg="black")
        
b6.pack()
b6.place(height=50,width=100, x=365, y=225)
        
b7 = tkinter.Button(ttt, text="click",command = boardGame.callback7,fg="black")
        
b7.pack()
b7.place(height=50,width=100, x=35, y=375)
        
b8 = tkinter.Button(ttt, text="click",command = boardGame.callback8,fg="black")

b8.pack()
b8.place(height=50,width=100, x=200, y=375)
        
b9 = tkinter.Button(ttt, text="click",command = boardGame.callback9,fg="black")
        
b9.pack()
b9.place(height=50,width=100, x=365, y=375)
boardGame.makeBoard()

canvas.pack(fill=BOTH)
ttt.mainloop()
