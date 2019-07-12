# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        for i in range(1,len(array)):
            if array[i]%2==0:
                continue
            index=i
            value=array[i]
            for j in range(i-1,-1,-1):
                if array[j]%2:
                    break
                else:
                    array[j+1]=array[j]
                    index=j
            array[index]=value
        return array