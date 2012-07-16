def fitness(level_data, moves):
	level_data['score'] = 0
	for move in moves:
		level_data = update(level_data, move)	
		if move == ABORT:
			break;

	return level_data['collected']

def new_gene(length):
	s = ''
	for j in range(length):
		s = s + ACTIONS[random.randrange(0, 5)]
	return array.array("c", s)

def mutation(gene, percent):
	for i in range(int(percent*len(gene))):
		pos = random.randrange(0, len(gene))
		gene[pos] =  ACTIONS[random.randrange(0, 6)] 
	return gene

def crossover(gene1, gene2):
	pos = random.randrange(0, len(gene1))
	return (gene1[:pos] + gene2[pos:], gene2[:pos] + gene1[pos:])

# genes init
	GENES = 15
	solutions = []
	
	for i in range(GENES):
		solutions.append(genetic.new_gene(level_data['size'][0]*level_data['size'][1]))

	for iter in range (11):
		# evaluation
		fit = [fitness(level_data, s) for s in solutions]
		fit = [f - min(fit) + 0.01 for f in fit]
			
		# selection
		total = reduce(lambda x, y: x + y, fit) 
		probs = [f * 100 / total for f in fit]
		probs = [sum(probs[:p + 1]) for p in range(GENES)]
		chosen_solutions = []
		for i in range(GENES):
			x = random.randrange(0, 100)
			for j in range(GENES):
				if x <= probs[j]:
					break
			chosen_solutions.append(solutions[j])


		solutions = []
		for i in range(GENES):
			solutions.append(genetic.mutation(chosen_solutions[i], 0.2))

	fit = [fitness(level_data, s) for s in solutions]