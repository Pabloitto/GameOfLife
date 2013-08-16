import random

"""
    Copyright 2013 Juan Pablo Itto Dominguez , juanitto_40@hotmail.com

    This file represent the core of all logic in the game

    The universe of the Game of life is a infinite two-dimensional orthogonal 

    grid of square cells, each of which is in one of two possible states, 

    alive or dead =)
"""

class GameOfLife(object):

	__ALIVE = 1 #represent a alive cell
	__DEAD = 0 #represent a dead cell
	__FULL_LIFE = 100 #full life in percent
	__PERCENT_TO_INIT_LIFE = 90 # is the percent of cells alive or dead =)

	#works in console mode
	__ALIVE_CHAR = "+"
	__DEAD_CHAR = "-"

	"""Private functions"""

	#init the size of panel
	def __init__(self):
		#board 40 x 40
		self.width = 40
		self.heigth = 40

	# return if some node is alive or dead via Random
	def __get_random_life(self):
		result = None
		if random.randint(self.__DEAD, self.__FULL_LIFE) > self.__PERCENT_TO_INIT_LIFE:
			result = self.__ALIVE
		else:
			result = self.__DEAD
		return result

	
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
		if live_cells == 3 or (live_cells == 2 and current_state == self.__ALIVE):
			return self.__ALIVE
		return self.__DEAD

	
	#Every cell interacts with its eight neighbors, which are 
	#the cells that are horizontally, vertically, or diagonally 
	#adjacent. At each step in time(generation).
	def __get_alive_neighbors(self , x , y , board):

		alive_neighbors = 0

		current_position = board[x][y] # get current cell

		size = len(board) - 1
		
		#left - right and top - down
		
		if (x - 1) > 0:
			if board[x - 1][y] == self.__ALIVE:
				alive_neighbors = alive_neighbors + 1

		if (x + 1) <= size:
			if board[x + 1][y] == self.__ALIVE:
				alive_neighbors = alive_neighbors + 1

		if (y + 1) <= size:
			if board[x][y + 1] == self.__ALIVE:
				alive_neighbors = alive_neighbors + 1

		if (y - 1) > 0:
			if board[x][y - 1] == self.__ALIVE:
				alive_neighbors = alive_neighbors + 1

		#corners

		if (x - 1) > 0 and (y - 1) > 0:
			if board[x - 1][y - 1] == self.__ALIVE:
				alive_neighbors = alive_neighbors + 1

		if (x + 1) <= size and (y - 1) > 0:
			if board[x + 1][y - 1] == self.__ALIVE:
				alive_neighbors = alive_neighbors + 1

		if(y + 1) <= size and (x - 1) > 0:
			if board[x - 1][y + 1] == self.__ALIVE:
				alive_neighbors = alive_neighbors + 1

		if(y + 1) <= size and (x + 1) <= size:
			if board[x + 1][y + 1] == self.__ALIVE:
				alive_neighbors = alive_neighbors + 1

		return alive_neighbors

	"""Public functions - expose the API"""
	#Get a first board randomly
	def get_board(self):
		return [[self.__get_random_life() for col in range(self.width)] for row in range(self.heigth)]

	#This method aply the algorithm for update the life in panel
	def update_life(self , board):
		updated_board = [[0 for col in range(self.width)] for row in range(self.heigth)]
		for i , row in enumerate(board):
			for j , cell in enumerate(row):
				number_of_neighbors = self.__get_alive_neighbors(i , j, board);
				updated_board[i][j] = self.__change_state(cell , number_of_neighbors)
		return updated_board

	#For testing in console the board
	def paint_board(self , board):
		for row in board:
			print("\n")
			for cell in row:
				comodin = self.__DEAD_CHAR;
				if cell == self.__ALIVE:
					comodin = self.__ALIVE_CHAR
				print(comodin , end="")
