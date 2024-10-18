class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD=10**9 +7

        #count of even and odd indices
        even_count=(n+1)//2
        odd_count=n//2

        total_good_string= (pow(5,even_count,MOD)* pow(4,odd_count,MOD)) %MOD

        return total_good_string
