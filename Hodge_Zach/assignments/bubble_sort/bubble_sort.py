import random

a = []

for i in range(100):
    a.append(random.randint(0, 10000))

print a

def bubble_sort(lst):
    temp = 0
    end = len(lst)

    while end != 0:
        for i in range(end):
            if i != (end - 1) and lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                print lst
        end -= 1

bubble_sort(a)

print a
