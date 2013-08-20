import random
"""
    Copyright 2013 Juan Pablo Itto Dominguez , juanitto_40@hotmail.com

    This file represent the core of all logic in the game

    The universe of the Game of life is a infinite two-dimensional orthogonal 

    grid of square cells, each of which is in one of two possible states, 

    alive or dead =)
"""
class GameOfLife():

	_scala = 20

	def __init__(self , size):
		self._scala = int(size / self._scala)
		self.width = self._scala
		self.heigth = self._scala
		self.width_screen = size
		self.heigth_screen = size
		self.size_x = size / self.width
		self.size_y = size / self.heigth
		self.board = self.__get_board()

	#return the new state of node(depends of the neighbors alive)
	#1) Any live cell with fewer than two live neighbors dies,
	#   as if caused under-population
	#2) Any live cell with two live neighbors lives on to the next
	#   generation
	#3) Any Live cell with more than three live neighbors dies,
	#   as if by overcrowding
	#4) Any dead cell with exactly three live neighbors becomes a live cell,
	#   as if by reproduction
	def __change_state(self , current_state , live_cells):
		return live_cells == 3 or (live_cells == 2 and current_state)
			

	#Every cell interacts with its eight neighbors, which are 
	#the cells that are horizontally, vertically, or diagonally 
	#adjacent. At each step in time(generation).
	def __get_alive_neighbors(self , x , y):
		alive_neighbors = 0

		tupe_neighbors = (-1 , 0 , 1)

		size = len(self.board) - 1

		for index_x in tupe_neighbors:
			for index_y in tupe_neighbors:
				if (x + index_x) > 0 and (x + index_x) <= size:
					if (y + index_y) > 0 and (y + index_y) <= size:
						if index_x == 0 and index_y == 0:
							continue
						if self.board[x + index_x][y + index_y]:
							alive_neighbors+=1

		return alive_neighbors

    #get a empty board
	def __get_board(self):
		return [[False for col in range(self.width)] for row in range(self.heigth)]

	#Refresh board
	def update_life(self):
		updated_board = self.__get_board()
		for i , row in enumerate(self.board):
			for j , cell in enumerate(row):
				number_of_neighbors = self.__get_alive_neighbors(i , j);
				updated_board[i][j] = self.__change_state(cell , number_of_neighbors)
		self.board = updated_board
