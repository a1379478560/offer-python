# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        pre=pHead
        pHead=pHead.next
        post=pHead.next
        pre.next=None
        while post:
            pHead.next=pre
            pre=pHead
            pHead=post
            post=post.next
        pHead.next=pre
        return pHead
            