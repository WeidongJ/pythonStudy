#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from time import sleep

# 常用算法

# 二分法查找


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] == item:
            return item
        elif item < list[mid]:
            high = mid - 1
        else:
            low = mid + 1


ls = [2, 1, 6, -7, 9]

print(binary_search(ls, 2))


# 选择排序
def selected_sorted(list):
    new_arr = []
    for _ in range(len(list)):
        smalllest = list[0]
        smallext_index = 0
        for j in range(1, len(list)):
            if smalllest > list[j]:
                smalllest = list[j]
                smallext_index = j
        new_arr.append(list.pop(smallext_index))
    return new_arr


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
