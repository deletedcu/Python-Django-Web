import random
numbers = []
for index_rand in range(1, 100):
    x = random.randint(0, 10000)
    numbers.append(x)
def select_sort():
    for index in range(len(numbers) - 1):
        min_value = index
        for j in range (index, len(numbers)):
            if numbers[j] < numbers[min_value]:
                min_value = j
        numbers[index], numbers[min_value] = numbers[min_value], numbers[index]
        print numbers

select_sort()