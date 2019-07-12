# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        res=[]
        while head:
            res.append(head)
            head=head.next
        if k>len(res):
            return None
        if k==0:
            return None
        return res[-k]