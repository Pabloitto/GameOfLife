from GameOfLife import GameOfLife
import threading , time
from PyQt4 import QtGui, QtCore
import sys ,  random

"""
    Copyright 2013 Juan Pablo Itto Dominguez , juanitto_40@hotmail.com

    The universe of the Game of life is a infinite two-dimensional orthogonal 

    grid of square cells, each of which is in one of two possible states, 

    alive or dead =)   
"""

#Class Represet a threat for update QWidget
class MyQTThread(QtCore.QThread):

    __TIME_OUT = 1 #represent a time out for refreshing 1/4 for second

    #Pass the form for refreshing
    def __init__(self , form): 
        QtCore.QThread.__init__(self)
        self.form = form

    #override run in a cycle
    def run(self): 
    	while True:
    		self.form.refresh()
    		time.sleep(self.__TIME_OUT)

    #Init the thread
    def begin(self): 
        self.start()

#class Form is a QWidget, update with a qthread
class Form(QtGui.QWidget):

    __SIZE_CELL = 10

    #encapsule the board in the widget
    def __init__(self , game_of_life , board):
        super(Form, self).__init__()
        self.game_of_life = game_of_life
        self.board = board
        self.initUI()

    #Is call for initialize the widget
    def initUI(self):
        self.setWindowTitle('Game of life')
        self.setFixedSize(400, 400)
        self.show()

    #Override the paint event for draw in the widget
    def paintEvent(self,event):
    	qp = QtGui.QPainter()
    	qp.begin(self)
    	self.drawPoints(qp)
    	qp.end()

    #this function draw the life ;)
    def drawPoints(self,qp):
    	color = None
    	qp.setPen(QtCore.Qt.black)
    	brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
    	qp.setBrush(brush)

    	for i , row in enumerate(self.board):
    		for j , cell in enumerate(row):
    			node = self.board[i][j]
    			if node == 0: #the node is dead
    				color = QtGui.QColor(255, 255, 255) #paint background
    			else:
    				color = QtGui.QColor(0, 139, 0) # Hey is alive!!!, so, paint green like a tree =)
    			qp.fillRect((i * self.__SIZE_CELL) + 2, (j * self.__SIZE_CELL) + 2, self.__SIZE_CELL - 3 , self.__SIZE_CELL  - 3, color)
                
    	self.board = self.game_of_life.update_life(self.board)

    #Refresh the widget
    def refresh(self):
    	self.update()

#Function main
def main():
    game_of_life = GameOfLife()
    board = game_of_life.get_board()
    app = QtGui.QApplication(sys.argv)
    win = Form(game_of_life , board)
    thread = MyQTThread(win)
    thread.begin()


    sys.exit(app.exec_())

#Execute main
main()
