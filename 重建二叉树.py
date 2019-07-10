# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if pre:
            head=TreeNode(pre[0])
        i=tin.index(pre[0])
        if i!=0:
            head.left=self.reConstructBinaryTree(filter(lambda x:x in tin[0:i],pre),tin[0:i])
        if i!=len(tin)-1:
            head.right=self.reConstructBinaryTree(filter(lambda x:x in tin[i+1:],pre),tin[i+1:])
        return head
        