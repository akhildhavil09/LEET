class Solution:
    def reverse(self, x: int) -> int:
        res=0
        max_int= 2**31-1
        sign=-1 if x<0  else 1
        x= abs(x)

        while x>0:
            temp=x%10
            if res>max_int //10 or (res==max_int //10 and temp>7):
                return 0
            res= res*10+temp
            x=x//10

        return sign* res