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

    __TIME_OUT = 0.25 #represent a time out for refreshing

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

    __is_started = False

    #encapsule the board in the widget
    def __init__(self , game_of_life):
        super(Form, self).__init__()
        self.game_of_life = game_of_life
        self.thread = MyQTThread(self)
        self.startButton = QtGui.QPushButton('Start', self)
        self.initUI()

    #Handler to excecute when start button is press
    def onClickButton(self):
        if not self.__is_started:
            self.thread.begin()
            self.startButton.setText("Stop")
        else:
            self.startButton.setText("Start")

        self.__is_started = not self.__is_started


    #Is call for initialize the widget
    def initUI(self):
        self.setWindowTitle('Game of life')
        self.setFixedSize(self.game_of_life.width_screen, self.game_of_life.heigth_screen)
        mainLayout = QtGui.QHBoxLayout()
        QtCore.QObject.connect(self.startButton, QtCore.SIGNAL("clicked()"), self.onClickButton)
        mainLayout.addWidget(self.startButton)
        mainLayout.setAlignment(QtCore.Qt.AlignTop)
        self.setLayout(mainLayout)
        self.show()

    def mousePressEvent(self, event):
        x = int(event.pos().x() / self.game_of_life.size_x)#Get relative position in the widget
        y = int(event.pos().y() / self.game_of_life.size_y)
        self.game_of_life.board[x][y] = not self.game_of_life.board[x][y] #set the oposite value in cell
        self.update()

    #Override the paint event for draw in the widget
    def paintEvent(self,event):
    	qp = QtGui.QPainter()
    	qp.begin(self)
    	self.drawPoints(qp)
    	qp.end()

    #this function draw the life ;)
    def drawPoints(self,qp):
        qp.setPen(QtCore.Qt.black)
        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        qp.setBrush(brush)
        for i , row in enumerate(self.game_of_life.board):
            for j , cell in enumerate(row):
                color = (QtGui.QColor(255, 255, 255), QtGui.QColor(0, 139, 0))[self.game_of_life.board[i][j]]
                qp.fillRect((i * self.game_of_life.size_x) + 2, (j * self.game_of_life.size_y) + 2, self.game_of_life.size_x - 3 , self.game_of_life.size_y  - 3, color)
        if self.__is_started:
            self.update_board()

    #This function update the life in the board
    def update_board(self):
        self.game_of_life.update_life()
    
    #Refresh the widget
    def refresh(self):
    	self.update()

#Function main
def main():
    """Configure board"""
    size = 400
    game_of_life = GameOfLife(size)
    app = QtGui.QApplication(sys.argv)
    win = Form(game_of_life)
    sys.exit(app.exec_())

#Execute main
main()
