class Solution:
    def twoSum(self, nums, target: int) :
        for i in range(len(nums)):
                for x in range(i+1,len(nums)):
                    if target==nums[i]+nums[x]:
                        return i, x
                    

a = Solution()
print(list(a.twoSum([2,7,11,15],9)))

from inspect import signature

def d(a,b,c=1):
    pass
params = signature(d).parameters
print(params)

