x = [4, 6, 1, 3, 5, 7, 25]
def stars(x):
    for i in range(len(x)):
        if type([i]) == str:
            print x[0].lower() * len(x)
        else:
            print x[i] * "*"
