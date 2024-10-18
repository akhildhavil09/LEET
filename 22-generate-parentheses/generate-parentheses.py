class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res,stack=[],[]
        def par(left,right):
            if left==right==n:
                res.append("".join(stack))
                return
            
            if left<n:
                stack.append("(")
                par(left+1,right)
                stack.pop()
            
            if right<left:
                stack.append(")")
                par(left,right+1)
                stack.pop()
            
        par(0,0)
        return res