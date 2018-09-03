# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 23:57:20 2018

@author: singh
"""

from tkinter import *
import tkinter.messagebox
import numpy as np

#makes board lines
def makeBoard():
    canvas.create_line(167,0,167,500, fill = 'red')
    canvas.create_line(334,0,334,500, fill = 'red')
    canvas.create_line(0,167,500,167, fill = 'red')
    canvas.create_line(0,334,500,334, fill = 'red')

    
#update x and o's
def update(index1, index2):
    board[index1,index2] = 1
    
    
#make game board filled with 0's
board = [[0,0,0],[0,0,0],[0,0,0]]

ttt = Tk()
ttt.title("tic tac toe")
ttt.geometry('500x500')

canvas = Canvas(ttt, width = 500, height = 500, bg = 'black')
makeBoard()

b1 = tkinter.Button(ttt, text="press",fg="black")

b1.pack()
b1.place(height=50,width=100, x=35, y=50)
canvas.pack(fill=BOTH)
ttt.mainloop()

    

