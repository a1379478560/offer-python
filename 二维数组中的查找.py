# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        leni=len(array)
        lenj=len(array[0])
        i,j=0,lenj-1
        while i<leni and j>=0:
            if array[i][j]==target:
                return True
            if target > array[i][j]:
                i+=1
                continue
            if target <array[i][j]:
                j-=1
                continue
        return False