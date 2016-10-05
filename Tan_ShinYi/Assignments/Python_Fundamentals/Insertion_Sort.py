import time
import random

nums = []

for i in range(100):
    nums.append(int((random.random())*10000)) #fills empty nums list with 100 random int's from 0-1000

print "Before everything happens:", nums

start_time=time.time() #records start time of sorting
for index1 in range(1, len(nums)):
    for index2 in range (0,index1):
        if nums[index1]<nums[index2]:
            temp=nums[index1]
            del nums[index1] #works much better than .remove(element) in this scenario
            nums.insert(index2, temp)

elapsed_time = time.time()-start_time #saves time elapsed for sorting
print "After everything happens:", nums
print 'Elapsed time taken for sorting (microseconds): ' + str(elapsed_time)
