def addTwoNumbers(l1,l2):
    pass

# 倒序输出整形
class Solution:
    def reverse(self, x: int) -> int:
        num = str(abs(x))
        if x>=0:
            return int(num[::-1])*(int(num[::-1])<2**31)
        else:
            return -int(num[::-1])*(int(num[::-1])<2**31)