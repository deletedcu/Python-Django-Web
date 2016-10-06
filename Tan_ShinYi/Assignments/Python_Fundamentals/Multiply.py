def multiply(a_list, multiplier):
    for i in range(len(a_list)):
        a_list[i]*=multiplier
    return a_list

print multiply([2,4,10,16],5)
