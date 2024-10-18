class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        sign=1
        index=0

        if index < len(s) and s[index] in ('-','+'):
            if s[index]=='-':
                sign =-1
            index+=1

        num=0
        while index<len(s) and s[index].isdigit():
            digit=int(s[index])
            num=num*10+digit
            index+=1

        num*=sign

        minimum, maximum= -2**31, 2**31 -1
        if num<minimum:
            return minimum
        if num> maximum:
            return maximum
        return num            
