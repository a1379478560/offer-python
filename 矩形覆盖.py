# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number==0:
            return 0
        if number==1:
            return 1
        if number==2:
            return 2
        res=[1,2]
        i=3
        while i<=number:
            res[0],res[1]=res[1],res[0]+res[1]
            i+=1
        return res[-1]