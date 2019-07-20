# -*- coding:utf-8 -*-
class Solution:
    def printMatrix(self, matrix):
        res=[]
        while matrix:
            res+=matrix.pop(0)
            if matrix and matrix[0]:
                for x in matrix:
                    res.append(x.pop())
            if matrix and matrix[0]:
                res+=matrix.pop(-1)[::-1]
            if matrix and matrix[0]:
                for x in matrix[::-1]:
                    res.append(x.pop(0))
        return res