# coding: utf-8
#  int a; int b
# 问 a//b + a//(b-1) + ... + a//2 + a//1

class Solution(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def f1(self, ):
        a=self.a; b=self.b
        b = min(a,b)
        ans = 0
        for i in range(1,b+1):
            ans += a//i
        return ans
    
    def f2(self,):
        a=self.a; b=self.b
        b = min(a,b)
        ans = 0
        # (0,1], (1,2], ... ,(a//3, a//2], (a//2, a],
        n, s = divmod(a,b)
        # 划分 a**0.5

        if n <= a**0.5:
            ans += (b - a//(n+1)) * n
            for i in range(n+1, int(a**0.5 + 1)):
                ans += (a//i - a//(i+1)) * i
            b = int(a**0.5) - 1
        # 以上已解决[a**0.5, b]

        # for i in range(n+1, a+1):
        #     print(a//i, a//(i+1))
        #     ans += (a//i - a//(i+1)) * i
        # 改为枚举1-a**0.5
        for i in range(1, b+1):
            ans += a//i
        return ans

s = Solution(25,5)
print(s.f1())
print(s.f2())