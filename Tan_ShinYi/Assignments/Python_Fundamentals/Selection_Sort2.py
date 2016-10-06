import time
import random

nums = []

for i in range(100):
    nums.append(int((random.random())*100)) #fills empty nums list with 100 random int's from 0-1000

print nums
start=0
end=len(nums)-1

start_time=time.time() #records start time of sorting
while (end-start)>0:
    min_place=start
    max_place=start
    for i in range(start,end+1): #this range shortens each round starting from the edge of the list and working inwards
        if nums[i]<nums[min_place]:
            min_place=i #finds the index of the min value in range
        elif nums[i]>nums[max_place]:
            max_place=i #finds the index of the max value in range
    nums[start], nums[min_place]=nums[min_place], nums[start] #swaps the min value with the value at the beginning of range
    if start == max_place: #if the value at the beginning of the range was the max value,
        max_place = min_place #assign max_place (max value index) to now be equal to where the min value was, before the swap
    nums[end], nums[max_place]=nums[max_place], nums[end] #swap end value with max value
    end-=1
    start+=1 #decrease range

elapsed_time = time.time()-start_time #saves time elapsed for sorting
print nums
print 'Elapsed time taken for sorting (microseconds): ' + str(elapsed_time)
