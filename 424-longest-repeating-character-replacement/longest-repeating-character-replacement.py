class Solution(object):
    def characterReplacement(self, s, k):
        init={}
        l,freq=0,0
        for r in range(len(s)):
            init[s[r]]= 1+ init.get(s[r],0)
            freq= max(freq,init[s[r]])

            if (r-l+1)- freq > k:
                init[s[l]]-=1
                l+=1
        return (r-l+1)