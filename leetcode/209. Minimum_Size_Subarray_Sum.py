# -*- coding: utf-8 -*-

# 时间复杂度O(n2) 不通过
class Solution:
    def minSubArrayLen(self, s: int, nums: [int]) -> int:
        minimum = float('inf')
        l = 0
        for i in range(len(nums)):
            s_sum = 0
            for j in range(i,len(nums)):
                s_sum += nums[j]
                if s_sum >= s:
                    l = j - i +1
                    break
            minimum = min(minimum, l)
        return minimum if minimum != float('inf') else 0
l = [1,4,4]
a = Solution().minSubArrayLen(4,l)
print(a)
#print(list(range(0,5)))

# solution2 

class Solution2:
    '''
    使用2个指针，右指针在不断的累加和直到sum >=s,此时判断子串的长度，左指针从sum中减去位于子串头部的元素，循环
    '''
    def minSubArrayLen(self, s: int, nums: [int]) -> int:
        s_sum = 0
        j = 0
        res = float('inf')
        for i in range(len(nums)): # 右指针累加
            s_sum += nums[i]
            while s_sum >= s: # 判断子串长度，左指针去除元素
                res = min(i-j+1,res)
                s_sum -= nums[j] 
                j += 1
        return res if res != float('inf') else 0

'''
binary search ：
1. sum list 存储所有的和，
sum[0] = 0 
sum[i] += sum[i-1] + nums[i] for i in range(len(nums))
2.可知sum是个有序的数组，假设 sum[i] + s 是我们要在sum数组中查找的目标值，
则当sum[j] >= sum[i] +s时有：sum[j]-sum[i] == 目标子串的和 >= s
'''


class Solution3:
    '''
    binary search
    '''
    def binary_search(self,low :int, nums: [list], target: int):
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) //2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid -1
        return low # low 即是sum[j] >= sum[i] +s 时 j的最小下标

    '''
    使用2个指针，右指针在不断的累加和直到sum >=s,此时判断子串的长度，左指针从sum中减去位于子串头部的元素，循环
    '''
    def minSubArrayLen(self, s: int, nums: [int]) -> int:
        s_sum = [0] * (len(nums) +1)
        for i in range(1,len(nums)+1): # 创建sum数组
            s_sum[i] = s_sum[i-1] + nums[i-1] 
        res = float('inf')
        for i in range(0,len(s_sum)): # 遍历sum数组
            to_find = s_sum[i] + s
            index = self.binary_search(i+1,s_sum,to_find) # low 直接设置成i+1,因为此时to_find = s_sum[i] + s > s_sum[i],从0下标开始没有意义
            if index == len(s_sum):
                break
            res = min(res,index-i)
        return res if res != float('inf') else 0
        

