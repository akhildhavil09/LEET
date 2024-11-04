class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        XOR_RESULT= start^goal
        #count the number of set bits in xor
        return bin(XOR_RESULT).count('1')