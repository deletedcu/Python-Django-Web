import random
import datetime

def selectsort(list):
    start = datetime.datetime.now()
    for i in range(len(list)):
        minIndex = i

        for j in range(i,len(list)):
            if list[minIndex] > list[j]:
                minIndex=j

        #print('List before swap: ', str(list))
        (list[minIndex], list[i])=(list[i], list[minIndex])
        #print('List after swap: ', str(list))
    end = datetime.datetime.now()
    return end - start

sample= [9,8,3,4,0,1]
selectsort(sample)

randomList =[]

for index in range(10000):
    randomList.append(random.randint(0,10000))

print('Random Number list of 10000 values')
runningtime = selectsort(randomList)
print('Starting list: ', randomList)
selectsort(randomList)
print('Ending list: ', randomList)
print( 'Running time: (hh:mm:ss.microsec) ',runningtime )
