# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        num=0
        if n<0:
            n=2**32+n
        while n:
            num+=n%2
            n=n//2
        return num