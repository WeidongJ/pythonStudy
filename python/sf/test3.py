#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 二分查找
def binary_search(l, item):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == item:
            return mid
        elif l[mid] < item:
            low = mid + 1
        else:
            high = mid -1

l = list(range(20))
print(l)
print(binary_search(l,15))


# 选择排序
def selection_sorted(l):
    new_arr = []
    for _ in range(len(l)):
        smallest = l[0]
        smallest_index = 0
        for i in range(1, len(l)):
            if smallest >= l[i]:
                smallest = l[i]
                smallest_index = i
        new_arr.append(l.pop(smallest_index))
    return new_arr

l2 = [2,-3,6,7,1]

print(selection_sorted(l2))


# 冒泡排序
def bubble_sorted(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - i -1):
            if l[j] >= l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

l3 = [2,-3,6,7,1]
print(bubble_sorted(l3))


# 快速排序
def quick_sorted(l):
    if len(l) < 2:
        return l
    povit = l[0]
    less = [i for i in l[1:] if i <= povit]
    more = [i for i in l[1:] if i > povit]
    return quick_sorted(less) + [povit] + quick_sorted(more)

l4 = [2,-3,6,7,1]
print(quick_sorted(l4))


# 进制转换
def convert(num,base=7):
    if num < base:
        return num
    return num % base + 10 * convert(num//base)

print(convert(70))