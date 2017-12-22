import random
import numpy as np
 
 # David F Greene
 
# neighborhood are point to the left right or up down
# local Optima/Max, goal/safe spot
# state space, configurations for game
# h is the pairs of queens attacking
 
 
print('8 Queens')
print ""
 
array = [[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0]]

 
# global variables
attacking_across = 0
total_attacks = 0
heuristic = 0
new_heuristic = 0
restart = "RESTART"
current = "Setting new current state"
state_changes = 0
restarts = 0
temp_array = []

 
# random rows for each column
def random_queens():

	global array
	array = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

	c = 0
	for ran in range(len(array)):
		r = random.randint(0,7) # random variables for queens
		# R  C
		array[r][c] = 1 # places queens in the array
		c += 1 # moves through columns
		
	return
 
 
def board(list):

	# variables
	global restarts

	check_across(array) # finds across attacks
	check_diagonal(array) # finds diagonal attacks
	
	print ""
	print "Current h: ", heuristic # displays current heuristic value
	print "Current State"
	
	# populates the board
	for y in range(len(array)): # row
		for x in range(len(array[y])): # col
			print array[y][x], # prints board
		print ""
		
	print "Neighbors found with lower h: " + str(new_heuristic) # updated heuristic value
	
	if (new_heuristic == 0):
		print restart
		print ""
		restarts += 1
	else:
		print current
		print ""
		
	# If solution is found
	if (heuristic == 0 and new_heuristic == 0):
		print "Solution Found!"
		print "State changes: ", state_changes
		print "Restarts: ", restarts
	
	return
 
 
# looking for possible cross attacks
def check_across(array):

	# variables
	queens = 0
	queens_rows = 0
	global attacking_across
   
	for rows in range(8): # row
		for col in range(8): # col
			if array[rows][col] == 1: # if found queen
				queens_rows += 1 # increment for queens
				queens += 1 # single queen
				if queens_rows > 1: # for across attacks
					attacking_across += (queens_rows - 1) # triangle number to find attacks

		queens_rows = 0 # reset for new row
   
	return
    

# looking for possible diagonal attacks	
def check_diagonal(array):
 
	# variables
	diagonal_attacks = 0
	global total_attacks
	global heuristic
   
	for rows in range(8): # row
		for col in range(8): # col
			if array[rows][col] == 1: # if found queen
				
				r = rows # resets
				c = col
				
				# down, right 
				while (r < 7 and c < 7): # checks for additional queens
					r += 1 # moving 
					c += 1
					if (array[r][c] != 0): # add if you find a queen
						diagonal_attacks += 1
					
						if diagonal_attacks > 1: # for diagonal attacks
							total_attacks += (diagonal_attacks - 1)
							diagonal_attacks = 0 # reset for new diagonal
						else:
							total_attacks += diagonal_attacks # single attacks
						
				r = rows # resets
				c = col
				
				# down, left
				while (r < 7 and c > 0): # checks for additional queens
					r += 1 # moving 
					c -= 1
					if (array[r][c] != 0): # add if you find a queen
						diagonal_attacks += 1
						
						if diagonal_attacks > 1: # for diagonal attacks
							total_attacks += (diagonal_attacks - 1)
							diagonal_attacks = 0 # reset for new diagonal
						else:
							total_attacks += diagonal_attacks # single attacks
								
		diagonal_attacks = 0 # reset for new diagonal
		
	heuristic = (attacking_across + total_attacks) # calculates all attacks
	
	return
	
	
def neighbors():

	# variables
	global total_attacks
	global heuristic
	global new_heuristic
	global attacking_across
	global state_changes
	
	flip_array = list(map(list, zip(*array))) # flips the array so it can read
	best_flipped = []
	lowest_h = 99
	
	# lower heuristic
	while heuristic > 0:
		for col_index, col in enumerate(flip_array):
			for row in range(len(col)):
				new_col = [0 if i != row else 1 for i in range(len(col))] # find columns
				new_array = flip_array[:col_index] + [new_col] + flip_array[col_index + 1:] # new flipped array
				total_attacks = heuristic = attacking_across = 0
				check_across(list(map(list, zip(*new_array)))) # calls checks for cross attacks
				check_diagonal(list(map(list, zip(*new_array)))) # calls checks for diagonal attacks
				if heuristic < lowest_h: 
					lowest_h = heuristic
					best_flipped = flip_array
					new_heuristic += 1
		total_attacks = heuristic = attacking_across = 0 # adds in total attacks
		board(list(map(list, zip(*best_flipped))))
		if new_heuristic == 0:
			random_queens()
			flip_array = list(map(list, zip(*array)))
			lowest_h = 99
		else:
			flip_array = best_flipped
		new_heuristic = 0
			
	return
   
random_queens() # inserts queens in board

board(array) # prints board

neighbors() # prints board

