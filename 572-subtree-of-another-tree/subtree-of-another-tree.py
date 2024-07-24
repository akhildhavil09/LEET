# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        def issame(p,q):
            if not p and not q: return True
            if not p or not q: return False
            if p.val!=q.val: return False

            return issame(p.left, q.left) and issame(p.right, q.right)

        def subsame(p,subRoot):
            if not p: return False
            if issame(p,subRoot): return True

            return subsame(p.left,subRoot) or subsame(p.right,subRoot)

        return subsame(root,subRoot)