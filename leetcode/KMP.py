# -*- coding: utf-8 -*-

# 返回子串T在主串第pos个字符后的位置

#暴力破解
def get_index_of_substring(T,S,pos=0):
    # 判断 T S不为空，pos > len(S) - len(T)
    if not T or not S or len(S) - len(T) < 0 or  pos > len(S) - len(T):
        print('Invalid string or pos!')
        return False
    # 遍历主串，pos< i < len(S) - len(T) +1
    for i in range(pos,len(S)-len(T)+1):
        # 主串开始位置确定后，遍历子串
        for j in range(len(T)):
            # 匹配主串和子串字符，遇见不相等就终止子串循环，进入主串下一次循环
            if S[i + j] != T[j]:
                break
            # 字串完成遍历即在主串中找到了子串，返回主串开始的位置i
            if j == len(T) -1:
                return i
    # 主串中不存在子串
    return False

print(get_index_of_substring('ab','aaaabaa',1))

class KMP(object):

    def __init__(self,t,text):
        self.t = t
        self.text = text

    def get_next(self):
        next = [0]*len(self.t)
        i = 1
        j = 0
        while i < len(self.t):
            # 判断前缀字符t[j-1]和后缀字符t[i-1]
            if j==0 or self.t[i-1]==self.t[j-1]:
                j += 1 # 前缀字符串长度
                i += 1
                # 如果前缀字符和当前字符不相等，则将前缀字符串长度赋值给next当前位置
                if self.t[i-1] != self.t[j-1]:
                    next[i-1] = j
                else:
                    next[i-1] = next[j-1]
                #print(next)
            else:
                j = next[j-1]
                # print('aaa')
        return next

    def get_index_of_substring(self):
        next = self.get_next()
        i = 1
        j = 1
        while i <= len(self.text) and j <= len(self.t):
            print(i,j,next)
            if j == 0 or self.text[i -1] == self.t[j -1]:
                i += 1
                j += 1
            else:
                j = next[j-1]
        if j > len(self.t) :
            return i - len(self.t)
        else:
            return False



T = KMP('ab','abcsabaaabaa')
#print(T.get_next())
print(T.get_index_of_substring())
    
