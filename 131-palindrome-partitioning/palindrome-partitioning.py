class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        res=[]
        path=[]

        dp=[[False]*n for _ in range(n)]

        for end in range(n):
            for start in range(end+1):
                if s[start]==s[end] and (end-start <=2 or dp[start+1][end-1]):
                    dp[start][end]=True
            
        def helper(index):
            if index==n:
                res.append(path[:])
                return
            
            for i in range(index,n):
                if dp[index][i]:
                    path.append(s[index:i+1])
                    helper(i+1)
                    path.pop()

        helper(0)
        return res