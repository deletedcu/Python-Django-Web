# PART 1

def draw_stars(x):
	for count in range(0, len(x)):
		print '*' * x[count]

x = [1, 2, 4, 8, 16, 32]
draw_stars(x)


# PART 2

def draw_star(x):
	for count in range(0, len(x)):
		if(isinstance(x[count], str)):
			print x[count].lower()[:1] * len(x[count])
		else:
			print '*' * x[count]