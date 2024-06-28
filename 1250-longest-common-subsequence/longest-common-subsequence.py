class Solution(object):
    def longestCommonSubsequence(self, t1, t2):
        dp=[[0 for j in range(len(t2)+1)] for i in range(len(t1)+1)]
        for a in range(i-1,-1,-1):
            for b in range(j-1,-1,-1):
                if t1[a]==t2[b]:
                    dp[a][b]=1+ dp[a+1][b+1]
                else:
                    dp[a][b]=max(dp[a+1][b],dp[a][b+1])
        return dp[0][0]

        