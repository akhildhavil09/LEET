# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        self.count=0
        self.result= None
        self.inorder(root,k)
        return self.result
    def inorder(self,node,k):
        if not node or self.count>k: return 

        self.inorder(node.left,k)
        self.count+=1

        if self.count==k:
            self.result= node.val
            return
        
        self.inorder(node.right,k)