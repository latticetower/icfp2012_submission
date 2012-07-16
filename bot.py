import signal
import sys
import re
import string
import pprint
import random
import array
import astar
import premade
from copy import deepcopy


WALL = '#'
ROBOT = 'R'
ROCK = '*'
EARTH = '.'
LIFT = 'L'
LIFT_OPEN = '0'
LAMBDA = '\\'
EMPTY = ' '
HOROCK = '@'
BEARD = 'W'
RAZOR = '!'

TRAMPOLINES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
TARGETS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

LEFT ='L'
RIGHT = 'R'
UP ='U'
DOWN = 'D'
WAIT = 'W'
ABORT = 'A'

WATER = 'Water'
FLOODING = 'Flooding'
WATERPROOF = 'Waterproof'
BREATH = 'Breath'

META = [WATER, FLOODING, WATERPROOF]

ACTIONS = [LEFT, RIGHT, UP, DOWN, WAIT, ABORT]
OPPOSITE = { LEFT: RIGHT, RIGHT: LEFT, UP: DOWN, DOWN: UP, '': '' }


def level_matrix(text):
	max_width = 0
	max_height = 0
	level_data = { 'tiles': {}, ROBOT: (0, 0), LIFT: (0, 0), 'size': (0, 0), 
				   'lambdas': [], 'rocks': [], 
				   'collected': 0, 'score': 0, 'turn': 0,
				   WATER: 0, FLOODING: 0, WATERPROOF: 0, BREATH: 0,
				   'dead': False }

	j = -1
	metamode = False
	for line in text:
		j = j + 1

		if line == '\n':
			metamode = True
			continue

		if not metamode:
			max_height += 1
			# read row
			row = list(line)[:len(line) - 1]
			if (max_width < len(row)) :
				max_width = len(row) 

			i = - 1
			for c in row:
				i = i + 1
				if c == ROBOT:
					level_data[ROBOT] = (i, j)
				elif c == LIFT:
					level_data[LIFT] = (i, j)
				elif c == LAMBDA:
					level_data['lambdas'].append((i, j))
				elif c == ROCK:
					level_data['rocks'].append((i, j))

				if c != ROBOT:
					level_data['tiles'][(i, j)] = { 'pos': (i, j), 'type': c, 'g': 0,  'h': 0,  'f': 0 }
				else:
					level_data['tiles'][(i, j)] = { 'pos': (i, j), 'type': EMPTY, 'g': 0,  'h': 0,  'f': 0 }
		else:
			# read metadata
			key, value = line.split()
			if key in META:
				level_data[key] = int(value)
				#print key, ".", level_data[key], "."
	

	level_data['size'] = (max_width, max_height)

	return level_data





def get_neighbour(level_data, node, move):

	this = (node['pos'][0], node['pos'][1])
	result = {}

	if move == LEFT:
		left = (this[0] - 1, this[1])
		if left[0] >= 0:
			if left in level_data['tiles']: 
				result = level_data['tiles'][left]

	if move == RIGHT:
		right = (this[0] + 1, this[1])
		if right[0] < level_data['size'][0]:
			if right in level_data['tiles']: 
				result =level_data['tiles'][right]

	if move == UP:
		top = (this[0], this[1] - 1)
		if top[1] >= 0:
			if top in level_data['tiles']: 
				result = level_data['tiles'][top]

	if move == DOWN:
		bottom = (this[0], this[1] + 1)
		if bottom[1] < level_data['size'][1]:
			if bottom in level_data['tiles']: 
				result = level_data['tiles'][bottom]

	return result

def move_rock(level_data, from_coord, to_coord):
	level_data['tiles'][from_coord]['type'] = EMPTY
	level_data['tiles'][to_coord]['type'] = ROCK
	level_data['rocks'].remove(from_coord)
	level_data['rocks'].append(to_coord)
	if (level_data[ROBOT] == (to_coord[0], to_coord[1] + 1)):
		level_data['dead'] = True

def update_water(level_data):

	if level_data[WATER] > 0:	
		if level_data[ROBOT][1] > level_data['size'][1] - level_data[WATER]:
			level_data[BREATH] += 1
		else:
			level_data[BREATH] = 0

	if level_data[BREATH] > level_data [WATERPROOF]:
		level_data['dead'] = True


	if level_data[FLOODING] != 0:
		if level_data['turn'] % level_data[FLOODING] == 0:
			level_data[WATER] += 1
			# print 'turn', level_data['turn']
			# print WATER, level_data[WATER]

	return level_data

def update(level_data, move):

	level_data['turn'] += 1
	# player turn
	if move == ABORT:
		level_data['score'] += 25*level_data['collected']
		return level_data

	level_data['score'] -= 1	
	if move != WAIT:
		neighbor = get_neighbour(level_data, level_data['tiles'][level_data[ROBOT]], move)
		if neighbor != {}:
			# scoring
			if neighbor['type'] == LAMBDA:
				level_data['score'] += 25
				level_data['collected']	+= 1
				if level_data['collected'] == len(level_data['lambdas']):
					level_data['tiles'][level_data[LIFT]]['type'] = LIFT_OPEN

			# movement
			if neighbor['type'] == LIFT_OPEN:
				level_data['score'] += 50*level_data['collected']

			if neighbor['type'] in [EMPTY, EARTH, LAMBDA, LIFT_OPEN]:
				level_data['tiles'][level_data[ROBOT]]['type'] = EMPTY
				level_data[ROBOT] = neighbor['pos']
				level_data['tiles'][level_data[ROBOT]]['type'] = ROBOT
				#print 'player moved to ', level_data[ROBOT]

			if neighbor['type'] == ROCK and move in [LEFT, RIGHT]:
				next_neighbor = get_neighbour(level_data, level_data['tiles'][neighbor['pos']], move)
				if next_neighbor['type'] == EMPTY:
					move_rock(level_data, neighbor['pos'], next_neighbor['pos'])
					level_data['tiles'][level_data[ROBOT]]['type'] = EMPTY
					level_data[ROBOT] = neighbor['pos']
					level_data['tiles'][level_data[ROBOT]]['type'] = ROBOT

	new_level = deepcopy(level_data)

	# update rocks
	for rock in level_data['rocks']:

		b_neighbor = get_neighbour(level_data, level_data['tiles'][rock], DOWN)

		if b_neighbor != {} and b_neighbor['type'] == EMPTY:
			# fall-down rule
			move_rock(new_level, rock, b_neighbor['pos'])
			continue
		
		if b_neighbor != {} and b_neighbor['type'] == ROCK:
			# fall-right rule
			r_neighbor = get_neighbour(level_data, level_data['tiles'][rock], RIGHT)
			if r_neighbor != {} and r_neighbor['type'] == EMPTY:
				rb_neighbor = get_neighbour(level_data, r_neighbor, DOWN)
				if rb_neighbor != {} and rb_neighbor['type'] == EMPTY:
					move_rock(new_level, rock, rb_neighbor['pos'])
					continue

			# fall-left rule
			if r_neighbor != {}:
				rb_neighbor = get_neighbour(level_data, r_neighbor, DOWN)
				if r_neighbor['type'] != EMPTY or rb_neighbor['type'] != EMPTY:
					l_neighbor = get_neighbour(level_data, level_data['tiles'][rock], LEFT)
					if l_neighbor != {} and l_neighbor['type'] == EMPTY:
						lb_neighbor = get_neighbour(level_data, l_neighbor, DOWN)
						if lb_neighbor != {} and lb_neighbor['type'] == EMPTY:
							move_rock(new_level, rock, lb_neighbor['pos'])
							continue

		if b_neighbor != {} and b_neighbor['type'] == LAMBDA:
			#  labmda fall-right rule
			r_neighbor = get_neighbour(level_data, level_data['tiles'][rock], RIGHT)
			if r_neighbor != {} and r_neighbor['type'] == EMPTY:
				rb_neighbor = get_neighbour(level_data, r_neighbor, DOWN)
				if rb_neighbor != {} and rb_neighbor['type'] == EMPTY:
					move_rock(new_level, rock, rb_neighbor['pos'])
					continue

	return new_level


def print_world(level_data):
	for j in range(0, level_data['size'][1]):
		line = ''
		for i in range(0, level_data['size'][0]):
			if (i, j) in level_data['tiles'].keys():
				line = line + level_data['tiles'][(i, j)]['type']
			else:
				line = line + ' '
		print line


def neighbors(level_data, node):
	result = []
	this = (node['pos'][0], node['pos'][1])

	left = (this[0] - 1, this[1])
	if left[0] >= 0:
		result.append((level_data['tiles'][left], LEFT))

	right = (this[0] + 1, this[1])
	if right[0] < level_data['size'][0]:
		if right in level_data['tiles']: 
			result.append((level_data['tiles'][right], RIGHT))

	top = (this[0], this[1] - 1)
	if top[1] >= 0:
		if top in level_data['tiles']: 
			result.append((level_data['tiles'][top], UP))

	bottom = (this[0], this[1] + 1)
	if bottom[1] < level_data['size'][1]:
		if bottom in level_data['tiles']: 
			result.append((level_data['tiles'][bottom], DOWN))

	return result


def optimize_moves(moves):
	moves = string.replace(moves, 'UDU', 'U')
	moves = string.replace(moves, 'DUD', 'D')
	moves = string.replace(moves, 'LRL', 'L')
	moves = string.replace(moves, 'RLR', 'R')
	return moves

def random_move(level_data, prev_move):

	ns = neighbors(level_data, level_data['tiles'][level_data[ROBOT]])
	cells, dirs = zip(*ns)

	variants = []

	# anti-drowning
	if level_data[WATER] > 0 and level_data[BREATH] > 0:
		if  level_data[ROBOT][1] - (level_data[WATERPROOF] - level_data[BREATH]) + 1 == level_data['size'][1] - level_data[WATER]:
			return UP
		elif level_data[ROBOT][1] - (level_data[WATERPROOF] - level_data[BREATH]) + 1 > level_data['size'][1] - level_data[WATER]:
			#print 'ROBOT', level_data[ROBOT]
			#print 'WATERPROOF', level_data[WATERPROOF]
			#print 'BREATH', level_data[BREATH]
			#print 'WATER', level_data[WATER]
			return ABORT


	for n in ns:
		if n[0]['type'] in [LAMBDA, LIFT_OPEN]:
			return n[1]

		if n[0]['type'] in [WALL, ROCK, LIFT]:
			continue

		if n[0]['type'] == EMPTY and n[1] == DOWN:
			if cells[dirs.index(UP)]['type'] == ROCK:
				continue

		variants.append(n[1])

	if len(variants) == 0:
		# escape from rock-trap
		for n in ns:
			if n[0]['type'] == ROCK:
				next_neighbor = get_neighbour(level_data, level_data['tiles'][n[0]['pos']], n[1])
				if next_neighbor['type'] == EMPTY:
					return n[1]
		# abort otherwise
		return ABORT
	
	if len(variants) == 1:
		return variants[0]
	else:
		# disallow backsteps
		if OPPOSITE[prev_move] in variants:
			variants.remove(OPPOSITE[prev_move])
		return variants[random.randrange(0, len(variants))]


def random_solver(level_data):
	result = ''
	move = ''
	while (move != ABORT) and (level_data[ROBOT] != level_data[LIFT]): 
		if len(result) == level_data['size'][0] * level_data['size'][1] - 1: 
			move = ABORT
		else:
			move = random_move(level_data, move)
		
		level_data = update_water(update(level_data, move))

		if level_data['dead']:
			move = ABORT

		result += move
		result = optimize_moves(result)

	return (result, level_data['score'])

def new_gene(length):
	s = ''
	for j in range(length):
		s = s + ACTIONS[random.randrange(0, 5)]
	return array.array("c", s)

def main():

	solution = 'LDLDDRUUURRDDDLLUULDRUULDRDDLURDRRRRDDLLLLLDRRULDLURRRURDRULDRUURA'

	def get_solution():
		return solution
	def signal_handler(signal, frame):
		print get_solution()
		sys.exit(0)



	signal.signal(signal.SIGINT, signal_handler)

	text = sys.stdin.readlines()
	'''prem = premade.check_premade(''.join(text))
	if prem != '':
		print prem
		return'''

	level_data = level_matrix(text)
	#pprint.pprint(level_data)
	best_score = -float('inf')

	solutions = []
	#'''
	for i in range (1000):
		s = random_solver(deepcopy(level_data))
		solutions.append(s)
		if s[1] > best_score:
			best_score = s[1]
			solution = s[0]

	print solution
	#'''

	'''
	moves = 'LLUUURUURRRRRRUULLLLLLDLDDRDLDRULDLDDRRUA'
	for m in moves:
		print m
		level_data = update_water(update(level_data, m))
		#print level_data['rocks']
	'''

	



if __name__ == "__main__":
	main()