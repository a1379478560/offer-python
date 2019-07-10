# -*- coding:utf-8 -*-

#其实一行 return 2**(number-1)就行了 自己做的有点麻烦了
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number==0:
            return 1
        if number==1:
            return 1
        if number ==2:
            return 2
        x=0
        for i in range(1,number+1):
            x+=self.jumpFloorII(number-i)
        return x

