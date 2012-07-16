def find_cheapest(node_set):
	min_cost = float('Inf')
	result = {}
	for k in node_set:
		if k['f'] < min_cost:
			min_cost = k['f']
			result = k
	return k

def dist(coord1, coord2):
	return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def h_dist_to_goal(start, goal):
	return abs(start['pos'][0] - goal['pos'][0]) + abs(start['pos'][1] - goal['pos'][1])

def h_dist_nearest_lambda(level_data, node):
	nearest = float('inf')
	for l in level_data.lambdas:
		d = dist(node['pos'], l)
		if d < nearest:
			nearest = d
	return nearest


'''
level_data - 
node - current node
'''
def neighbors(level_data, node):
	result = []
	this = (node['pos'][0], node['pos'][1])

	left = (this[0] - 1, this[1])
	if left[0] >= 0:
		result.append( level_data['tiles'][left])

	right = (this[0] + 1, this[1])
	if right[0] < level_data['size'][0]:
		if right in level_data['tiles']: 
			result.append( level_data['tiles'][right])

	top = (this[0], this[1] - 1)
	if top[1] >= 0:
		if top in level_data['tiles']: 
			result.append( level_data['tiles'][top])

	bottom = (this[0], this[1] + 1)
	if bottom[1] < level_data['size'][1]:
		if bottom in level_data['tiles']: 
			result.append( level_data['tiles'][bottom])

	return result

def reconstruct_path(level_data, start, goal):
	result = []
	current = goal
	
	while True:
		result.append(current['pos'])
		#print current
		if 'from' in current.keys():
			current = level_data['tiles'][current['from']]
		else:
			break

	return result


def a_star(level_data, start, goal):

	start['g'] = 0
	start['h'] = h_dist_to_goal(start , goal)
	start['f'] = start['g'] + start['h']

	closed_set = []
	open_set =  { start['pos']: start }

	lambdas = 0;


	while len(open_set.keys()) > 0:
		current = find_cheapest(open_set.values())
		if current['pos'] == goal['pos']:
			return reconstruct_path(level_data, start, goal)

		open_set.pop(current['pos'])
		closed_set.append(current['pos'])

		for y in neighbors(level_data, current):
			if y['pos'] in closed_set:
				continue
			tentative_g = current['g'] + costs[current['type']]

			if y['pos'] not in open_set.keys():
				open_set[y['pos']] = y
				tentative_better = True
			else:
				if tentative_g < y['g']:
					tentative_better = True
				else:
					tentative_better = False

			if tentative_better:
				y['from'] = current['pos']
				y['g'] = tentative_g
				y['h'] = h_dist_to_goal(y, goal)
				y['f'] = y['g'] + y['h']
	return 'A'