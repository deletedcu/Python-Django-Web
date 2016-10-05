# Part 1

#print 'Enter a list of at least 2 numbers seperated by commas:'
#x = input()
#def draw_starz(x):
#	count = 0
#	while (count < len(x)):
#		print x[count] * '*'
#		count += 1

#draw_starz(x)

# Part 2

y = [4, 'Tom', 1, 'Michael', 5, 7, 'Jimmy Smith']
def draw_starz2(list):
	for x in list:
		output = ''
		if type(x) is int:
			for i in range(x):
				output += '*'
		elif type(x) is str:
			first = x[0].lower()
			for i in range(len(x)):
				output += first
		print output
draw_starz2(y)

