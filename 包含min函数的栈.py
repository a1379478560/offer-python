# -*- coding:utf-8 -*-
class Solution:
    def __init__(self,):
        self.stack=[]
        self.minV=[]
    def push(self, node):
        self.stack.append(node)
        if self.minV and self.minV[-1]<node:
            return
        self.minV.append(node)
    def pop(self):
        if not self.stack:
            return None
        if self.stack[-1]==self.minV[-1]:
            self.minV.pop()
        return self.stack.pop()
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]
    def min(self):
            return self.minV[-1]