class Solution:
    def reverse(self, x: int) -> int:
        maxint= 2**31-1
        sign= -1 if x<0 else 1
        res=0
        x=abs(x)

        while x>0:
            digit= x%10
            if res>maxint//10 or (res==maxint//10 and digit>7):
                return 0
            res=res*10+digit
            x=x//10

        return sign*res
