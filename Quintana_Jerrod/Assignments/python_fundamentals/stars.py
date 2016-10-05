x = [4,6,1,3,5,7,25]
y = [4, 'Tom', 1, 'Michael', 5, 7, 'Jimmy Smith']
def draw_stars (arr):
    for element in range(0,len(arr)):
        if (type(arr[element]) == str ):
            draw = arr[element][0]
            print draw * len(arr[element])
        else:
            draw = '*'
            print draw*arr[element]
draw_stars(x)
draw_stars(y)
