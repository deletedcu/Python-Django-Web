def draw_stars(list):
    for value in list:
        if type(value) is int:
            print "*" * value
        else:
            print value[0].lower() * len(value)

draw_stars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
