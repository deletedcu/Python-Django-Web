
def draw_stars(list_o_nums):

    for i in range(len(list_o_nums)):
        print '*'*list_o_nums[i]

a= [4,3,5]
print a
draw_stars(a)

def draw_stars2(list_o_rand):
    for i in range(len(list_o_rand)):
        if type(list_o_rand[i])== int:
            print '*'*list_o_rand[i]
        elif type(list_o_rand[i])==str:
            print list_o_rand[i][0].lower()*len(list_o_rand[i])

b=[4, 'Tom', 3, 'Michael', 5]
print b
draw_stars2(b)
