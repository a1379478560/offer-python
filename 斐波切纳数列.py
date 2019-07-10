# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        res=[0,1,1,2]
        i=4
        while i<=n:
            res.append(res[-1]+res[-2])
            i+=1
        return res[n]