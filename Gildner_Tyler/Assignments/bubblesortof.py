arr = [1, 9, 90, 15, 29, 2, 8, 4, 70, 23, 3, 10]

def bubblesortof(arr):
    swaps = True
    next = len(arr)-1
    while next > 0 and swaps:
        swaps = False
        for i in range(next):
            if arr[i] > arr[i + 1]:
                swaps = True
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        next = next - 1

bubblesortof(arr)
print(arr)
