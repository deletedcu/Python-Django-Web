#Create a function that multiply elements of a List by 5
def multiply(a,m):
    b = []
    for element in a:
        b.append(element * m)
    print b
a = [2,4,10,16]
m = 5
multiply(a,m)
