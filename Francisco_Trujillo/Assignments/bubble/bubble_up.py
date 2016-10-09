import random
import datetime

def bubble_sort(list):
    start = datetime.datetime.now()
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            print("Before Swap: " + str(list))
            if list[j]>list[j+1]:
                (list[j], list[j+1])= (list[j+1], list[j])
            print("After Swap: " + str(list))
    end = datetime.datetime.now()
    return end-start

mylist = [6,5,3,1,8,7,2,4]
bubble_sort(mylist)

randomList =[]

for index in range(100):
    randomList.append(random.randint(0,10000))
print('Random Number list of 100 values')
bubble_sort(randomList)
