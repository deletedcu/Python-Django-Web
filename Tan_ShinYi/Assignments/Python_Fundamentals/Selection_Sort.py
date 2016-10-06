import random

nums = []

for i in range(100):
    nums.append(int((random.random())*10000)) #fills empty nums list with 100 random int's from 0-1000

count=0


while count<(len(nums)-1):
    min_place=count
    for i in range(count,len(nums)):
        if nums[i]<nums[min_place]:
            min_place=i
    nums[count], nums[min_place]=nums[min_place], nums[count]
    count+=1

print nums #prints sorted list
