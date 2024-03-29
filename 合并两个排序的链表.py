# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:       # 非递归版本
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val<pHead2.val:
            head=p=ListNode(pHead1.val)
            pHead1=pHead1.next
        else:
            head=p=ListNode(pHead2.val)
            pHead2=pHead2.next
        while pHead1 and pHead2:
            if pHead1.val<pHead2.val:
                p.next=ListNode(pHead1.val)
                p=p.next
                pHead1=pHead1.next
            else:
                p.next=ListNode(pHead2.val)
                p=p.next
                pHead2=pHead2.next
        tmp=pHead1 or pHead2
        while tmp:
            p.next=ListNode(tmp.val)
            p=p.next
            tmp=tmp.next
        return head
        
#######################递归版本##############
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1==None:
            return pHead2
        if pHead2==None:
            return pHead1
        if pHead1.val<pHead2.val:
            pHead1.next=self.Merge(pHead1.next,pHead2)
            return pHead1
        else:
            pHead2.next=self.Merge(pHead1,pHead2.next)
            return pHead2