my_list =  [1,88,'butt',4,7,'chetan',10,25,'thecodingdojo']
def drawStars(x):
	for var in x:
		if type(var) == int:
			print '*'*var
		else:
			print var[0].lower()*len(var)

drawStars(my_list)
