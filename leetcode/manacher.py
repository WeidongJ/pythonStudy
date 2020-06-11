# -*- coding: utf-8 -*-

"""
给定一个字符串，然后输出这个字符串包含的最长回文子串。例如，"cbabfd" 的最长回文子串就是 "bab".
"""

class Solution:
    '''
    中心扩展算法：选择一个中心点，依次判断左右字符是否相等
    分析：由于字符串长度可能是奇数或者偶数，所以中心点可能是一个字符或者2个字符中间
    '''
    def expand(self,s,left,right):
        l = left
        r = right
        while l >=0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l -1

    def longestPalindrome(self,s):
        if not s:
            return False
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i+1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length-1) // 2
                end = i + length // 2
        return s[start:end +1]
a = Solution()
print(a.longestPalindrome('abdccdef'))

