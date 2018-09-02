# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 23:57:20 2018

@author: singh
"""

from tkinter import *
import tkinter.messagebox
import numpy as np

#make game board filled with 0's
board = [[0,0,0],[0,0,0],[0,0,0]]

ttt = Tk()
ttt.title("tic tac toe")
ttt.geometry('500x500')

canvas = Canvas(ttt, width = 500, height = 500, bg = 'white')
createBoard()

canvas.pack()
ttt.mainloop()


#makes board lines
def createBoard():
    canvas.create_line(167,0,167,500)
    canvas.create_line(334,0,334,500)
    canvas.create_line(0,167,500,167)
    canvas.create_line(0,334,500,334)
    
    

