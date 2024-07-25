class Solution(object):
    def isValidBST(self, root):
        def dfs(node,minval, maxval):
            if not node: return True
            if not (minval<node.val<maxval): return False

            return dfs(node.left,minval,node.val) and dfs(node.right,node.val, maxval)
        return dfs(root, float('-inf'),float('inf'))
        