class Solution(object):
    def longestPalindrome(self, s):
        res=""
        reslength=0 # since we need the max value
        for i in range(len(s)):
            #odd we need 1 char at center to expand
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if(r-l+1)>reslength:
                    res=s[l:r+1]
                    reslength= r-l+1
                l-=1
                r+=1
            #even we need 2 char at the center
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if(r-l+1)>reslength:
                    res=s[l:r+1]
                    reslength=r-l+1
                l-=1
                r+=1
        return res   
