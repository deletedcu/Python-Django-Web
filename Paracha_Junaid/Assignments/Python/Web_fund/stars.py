# x = [4, 6, 1, 3, 5, 7, 25]

# def stars (a):
# 	i = 0
# 	while (i < len(a)):
# 		print '*' * a[i]
# 		i += 1
# stars(x)	

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def stars (a):
	i = 0
	while (i < len(a)):
		if type(a[i]) is int:
			print '*' * a[i]
			i+=1
		else: 
			temp = a[i]
			temp = temp.lower()
			print (len(a[i])) * temp[0]
			i += 1
stars(x)	
