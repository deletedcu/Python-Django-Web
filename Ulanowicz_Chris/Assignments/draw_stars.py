def draw_stars(list):
	for i in list:
		if type(i) == int:
			print "*" * int(i)
		else:
			print i[0].lower() * len(i)

a = [4,"Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(a)
