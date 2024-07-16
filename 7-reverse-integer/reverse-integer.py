class Solution(object):
    def reverse(self, x):
        rev=0
        maxint= 2**31 -1
        sign= -1 if x<0 else 1
        x= abs(x)

        while x:
            digit=x%10
            
            if rev>maxint //10 or (rev==maxint //10  and digit >7):
                return 0
            rev= (rev*10) + digit
            
            x//=10
        return rev*sign