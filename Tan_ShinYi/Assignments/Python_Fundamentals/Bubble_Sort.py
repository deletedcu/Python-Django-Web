import random
import time

nums = []

for i in range(100):
    nums.append(int((random.random())*10000)) #fills empty nums list with 100 random int's from 0-1000

count=1

start_time=time.time() #records start time of sorting
while(len(nums)-count!=0):
    for i in range(len(nums)-count):
        if nums[i]>nums[i+1]: #if value of lower index is greater than value of higher index, swap those two values
            nums[i], nums[i+1]=nums[i+1], nums[i]
    count+=1

elapsed_time = time.time()-start_time #saves time elapsed for sorting
print nums #prints sorted list
print 'Elapsed time taken for sorting (microseconds): ' + str(elapsed_time)
