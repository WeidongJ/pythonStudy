# 二分法
def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low +high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid +1
        else:
            high = mid -1
    return None

# 选择排序
def selectionSorted(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = arr[0]
        smallest_index = 0
        for j in range(1,len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j
        newArr.append(arr.pop(smallest_index))

    return newArr

test_list = [1,3,6,8,9]
print(binary_search(test_list,1))
print(selectionSorted([5,3,6,2,10]))