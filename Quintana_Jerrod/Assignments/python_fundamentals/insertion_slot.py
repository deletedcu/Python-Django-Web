org = [6,5,3,1,8,7,2,4]
# goal is to sort through each element in a list and sort it from lowest on the left to highest on the right. When sorting it swaps itself with the element to its left, one at a time, without creating a new array
import random
import time
#these are so i can use random.random() and time so I can see how long it takes my program to run
new = []
for index in range(0,100):
    number = round(random.random() *10000)
    new.append(number)
#this simply creates a new array every time i run this file with random whole numbers from 1 to 1000
def swap(list, ind):
    while (list[ind] < list[ind -1]):
        if ind == 0:
            break
        temp = list[ind]
        list[ind] = list[ind -1]
        list[ind - 1] = temp
#This is a side function I created to be called within the main function which is below, this simply takes the place of swapping the values. I give it the current list i'm working on and the index of whatever I'm on in the main function when it's called (see below where it's called), it has a while loop that checks if the current index is smaller than the one before it. If it does, then it first checks if it's the first index and breaks, or it swaps with the one before it, then it is re-run, again and again until it's no longer smaller and is in its correct sorted place.

def insert(arr):
    start_time = time.time()
    #this is simply a variable that starts a clock when the program runs so I can see how long it takes
    for i in range(len(arr)):
        element = arr[i]
        #this first main loop iterates through the given list for every index, first creating a variable equaling what it's currently on to compare to every other index we hit. 2 loops is necessary so I can iterate through the entire array for each index so that each index can be moved where it needs to be, so if I have a list thats 5 indexes long, it loops through the entire list 5 times, for a total of 25 loops.
        for index in range(len(arr)):
            #this loop is so that I can move each index where it needs to be, it checks if each index is smaller than the one before, if it is, then I call the swap function to swap it as many times as necessary, though in hindsight the swap function is useless since I would have only had to write it once anyways, but it was good practice on calling functions within functions
            if arr[index] < element:
                swap(arr,index)
    print arr
    print ("--- %s seconds ---" % (time.time() - start_time))
insert(org)
insert(new)
