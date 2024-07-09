class Solution(object):
    def hammingWeight(self, n):
        c=0
        for i in bin(n):
            if i=="1":
                c+=1
        return c