class Solution(object):
    def lengthOfLongestSubstring(self, s):
        init={}
        l,r,res=0,0,0
        while r<len(s):
            if s[r] in init:
                if init[s[r]]>=l:
                    l=init[s[r]]+1
            len_sub= r-l+1
            res= max(res,len_sub)
            init[s[r]]=r        
            r+=1
        return res