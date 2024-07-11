class Solution(object):
    def reverse(self, x):
        rev_x= 0
        sign=-1 if x<0 else 1
        x=abs(x)

        maxint= 2**31 -1
        while x>0:
            digit= x%10

            if rev_x > maxint //10 or (rev_x== maxint //10 and digit>7):
                return 0
            rev_x= rev_x * 10 + digit
            x//=10
        return rev_x*sign