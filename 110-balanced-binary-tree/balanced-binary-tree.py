class Solution(object):
    def isBalanced(self, root):
        def dfs(root):
            if not root: return[True,1]
            left, right= dfs(root.left), dfs(root.right)

            balance= left[0] and right[0] and abs(left[1]-right[1])<=1

            return[balance,1+ max(left[1],right[1])]

        return dfs(root)[0]
        