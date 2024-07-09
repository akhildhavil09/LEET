class Solution(object):
    def getSum(self, a, b):
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # mask to get 32 bits integer
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ gets the sum without carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)
