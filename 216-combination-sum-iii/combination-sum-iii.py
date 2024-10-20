class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def helper(start, remaining, sub):
            #pruning early to avoid uncessary calculations
            if remaining<0 or len(sub)>k:
                return
            #sucess case
            if len(sub) == k and remaining == 0:
                res.append(sub[:])
                return
            
            for i in range(start,10):
                sub.append(i)
                helper(i+1, remaining-i, sub)
                sub.pop()
            
        helper(1,n,[])

        return res
