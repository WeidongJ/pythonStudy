from collections import deque

# 二分法


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

# 选择排序


def selectionSorted(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = arr[0]
        smallest_index = 0
        for j in range(1, len(arr)):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j
        newArr.append(arr.pop(smallest_index))

    return newArr


test_list = [1, 3, 6, 8, 9]
print(binary_search(test_list, 1))
print(selectionSorted([5, 3, 6, 2, 10]))

# 递归函数

# 列表累加


def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])


sum([6, 4, 7])

# 列表计数


def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])


count([2, 34, "", '12'])

# 求最大值


def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


max([1, 7, -3, 9])

# 快速排序


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        glter = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(glter)


quicksort([1, -54, 45, 23])

# 广度优先搜索


def person_is_seller(person):  # 指定名字最后以m结尾的是经销商
    return person[-1] == "y"


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller')
                return True  # return 会退出函数
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")


def sum1(a):
    while True:
        if a > 0:
            print(a)
            return True
        else:
            a += 1


sum1(3)
