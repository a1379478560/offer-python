# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray :
            return 0
        for i in range(1,len(rotateArray)):
            if rotateArray[i]<rotateArray[i-1]:
                return rotateArray[i]