


def draw_star(arr):
    for element in arr:
        if type(element) is int:
            print '*' * element
        else:
            print element[:1].lower() * len(element)


x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
y = [4, 6, 1, 3, 5, 7, 25]

draw_star(x)
draw_star(y)
