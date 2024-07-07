class Solution(object):
    def plusOne(self, digits):
        num= int(''.join(map(str,digits)))+1
        digits=[]
        digits=[int(digit) for digit in str(num)]
        return digits