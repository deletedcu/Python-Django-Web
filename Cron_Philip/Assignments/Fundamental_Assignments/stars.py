def draw_stars(input):
    for index in range(len(input)):
        if type(input[index]) is int: 
            print input[index] * '*'
        else:
            print input[index][0].lower() * len(input[index])

x = [4,6,1,3,5,7,25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(y)
