# This is my revised code
#first code you see is my original method revised to to shorten the if else statements and time.
#my first two codes were made upon the assumption we were making a new list and slowly pushing the lowest elements into the new list and out of the original list. second code is the original method and code.
#the third code is it without creating a new list, simply rearranging the original list
unsorted = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
#lines below are so that I can create a random list with 100 numbers in it and use the time function to see how long my code takes
import random
import time
new = []
for index in range(0,100):
    number = round(random.random() *1000)
    new.append(number)
#the function below is where I sort by creaitng a new array, taking each lowest number out of the initial array and putting it into the new list, I then changed the code to use a max and min varible to take both out of the initial list in one loop, cutting the computing time in half
def sort(list):
    start_time = time.time()
    sorted = []
    length = len(list)
    end = length - 1
    for index in range(len(list)/2):
        #I divided by two because, since i'm taking two indexes in one loop, i only have to use half the amount of loops
        min = list[0]
        max = list[0]
        for i in range(length):
            if list[i] < min:
                min = list[i]
            elif list[i] > max:
                max = list[i]
            #i find the min and maximum numbers in the loop and store them
        sorted.insert(index, min)
        sorted.insert(end, max)
        #I then put the new varible on the current index near the first half of the list, and the second half according to the end variable.
        end -= 1
        list.remove(min)
        list.remove(max)
        length -=2
    print sorted
    print ("--- %s seconds ---" % (time.time() - start_time))
'''sort(unsorted)
sort(new)'''

#This was my original code before I tried to get rid of all of the if else statements
'''unsorted = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]

import random
import time
new = []
for index in range(0,100):
    number = round(random.random() *1000)
    new.append(number)

def sort(list):
    start_time = time.time()
    sorted = []
    length = len(list)
    for index in range(len(list)):
        min = list[0]
        for i in range(length):
            if list[i] < min:
                min = list[i]
        sorted.append(min)
        list.remove(min)
        length -=1
    print sorted
    print ("--- %s seconds ---" % (time.time() - start_time))
sort(unsorted)
sort(new)
'''

'''
def selection(list):
    start = 0
    hold = 0
    for i in range (len(list)):
        min = list[start]
        for index in range (start, (len(list))):
            if list[index] < min:
                min = list[index]
                hold = index
        if min == list[start]:
            continue
        list.pop(hold)
        list.insert(start, min)
        start += 1
    print list
selection(unsorted)
selection(new)
'''
