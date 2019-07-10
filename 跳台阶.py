# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        ret=0
        if number==1:
            return 1
        if number==2:
            return 2
        a=number//2
        for i in range(0,a+1):
            ret+=self.C(i,number-i)
        return ret
    def C(self,i,m):
        ret=1
        for i in range(i):
            ret=ret*(m-i)/(i+1)
        return ret