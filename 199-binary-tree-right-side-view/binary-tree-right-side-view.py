# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root: return []
        res=[]

        q= deque([root])
        while q:
            size=len(q)
            for i in range(size):
                node=q.popleft()

                if i==size-1:
                    res.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return res

        