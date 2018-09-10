# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 23:57:20 2018
@author: singh, davidson
"""

from tkinter import *
import tkinter.messagebox
import numpy as np

turn=0

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
    b1.config(state=DISABLED)
    nextTurn()
    
def callback2():
    global turn
    turn +=1
    if(turn%2==0):
        b2.config(text="x")
        board[0][1]=0
    else:
        b2.config(text="o")
    b2.config(state=DISABLED)
    nextTurn()
    
def callback3():
    global turn
    turn +=1
    if(turn%2==0):
        b3.config(text="x")
        board[0][2]=0
    else:
        b3.config(text="o")
    b3.config(state=DISABLED)
    nextTurn()
    
def callback4():
    global turn
    turn +=1
    if(turn%2==0):
        b4.config(text="x")
        board[1][0]=0
    else:
        b4.config(text="o")
    b4.config(state=DISABLED)
    nextTurn()
    
def callback5():
    global turn
    turn +=1
    if(turn%2==0):
        b5.config(text="x")
        board[1][1]=0
    else:
        b5.config(text="o")
    b5.config(state=DISABLED)
    nextTurn()
    
def callback6():
    global turn
    turn +=1
    if(turn%2==0):
        b6.config(text="x")
        board[1][2]=0
    else:
        b6.config(text="o")
    b6.config(state=DISABLED)
    nextTurn()
    
def callback7():
    global turn
    turn +=1
    if(turn%2==0):
        b7.config(text="x")
        board[2][0]=0
    else:
        b7.config(text="o")
    b7.config(state=DISABLED)
    nextTurn()
    
def callback8():
    global turn
    turn +=1
    if(turn%2==0):
        b8.config(text="x")
        board[2][1]=0
    else:
        b8.config(text="o")
    b8.config(state=DISABLED)
    nextTurn()
    
def callback9():
    global turn
    turn +=1
    if(turn%2==0):
        b9.config(text="x")
        board[2][2]=0
    else:
        b9.config(text="o")
    b9.config(state=DISABLED)
    nextTurn()
    
def winCheck():
    if(board[0][0]==0 and board[0][1]==0 and board[0][2]==0):
        X=Label(ttt,text="x wins")
        
def nextTurn():
    global turn
    if(turn%2 == 0):
        hud.set("O's turn")
    else:
        hud.set("X's turn")
    if(turn >= 9):
        hud.set("game over")

#make game board filled with 0's
board = [[0,0,0],[0,0,0],[0,0,0]]

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
