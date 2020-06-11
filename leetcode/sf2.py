
# -*- coding: utf-8 -*-


from time import sleep

# 常用算法

# 二分法查找


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] > item:
            high = mid -1
        elif list[mid] < item:
            low = mid + 1
        else:
            return item
        # if list[mid] == item:
        #     return item
        # elif item < list[mid]:
        #     high = mid - 1
        # else:
        #     low = mid + 1
    return None


ls = [2, 1, 6, -7, 9]

print(binary_search(ls, 2))

ls = [2, 1, 6, -7, 9]
# 选择排序
def selected_sorted(arr):
    newArr = []
    for _ in range(len(arr)):
        smallest = arr[0]
        smallest_index = 0
        for i in range(1,len(arr)):
            if arr[i] < smallest:
                smallest =arr[i]
                smallest_index = i
        newArr.append(arr.pop(smallest_index))
    return newArr

def selected_sort(arr):
    smallest = arr[0]
    smallest_index = 0
    while len(arr) > 1:
        for i in range(1,len(arr)):
            if arr[i] < smallest:
                smallest =arr[i]
                smallest_index = i
        return [arr.pop(smallest_index)] + selected_sort(arr)
    return arr

print(selected_sort(ls))
a = [1,2]
b = [3,4]
print(a+b)

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        large = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(large)

def ojld(a,b):
    while a%b != 0:
        return ojld(b,a%b)
    return b
print(ojld(3, 2))

print(selected_sorted(ls))


ll = [2, 1, 6, -7, 9]

# 冒泡排序


def bubble_sorted(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


print(bubble_sorted(ll))

l = [1,2,3,4,5]
def get_last(l,k):
    i = k
    n = len(l)
    while(n>1):
        l.pop(i%n-1)
        print(i,n,l,i%n)
        i = k if i%n ==0 else i % n- 1 +k
        #i = k if i%n-1 == 0 else i + k-1
        n -= 1
    return l
    
print(get_last(l,3))
l = [1,2,3,4,5]
print(l.pop(-1))


# 快速排序
def quick_sorted(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i < pivot]
        glter = [i for i in list[1:] if i >= pivot]
    return less + [pivot] + glter


print(quick_sorted(ll))


a= [1,2,3]
a[3] = 4


