def selection_sort(list):
    for item in range(len(list)):
        min = list[item]
        for ele in range(item, len(list)):
            if min >= list[ele]:
                min = list[ele]
                index = ele
            if
        temp = list[item]
        list[item] = min
        list[index] = temp
    return list

list = [4,2,9,7,5,5,6,5,5]

print(selection_sort(list))
