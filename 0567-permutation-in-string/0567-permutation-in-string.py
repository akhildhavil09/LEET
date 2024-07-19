from itertools import permutations
class Solution(object):
    def checkInclusion(self, s1, s2):
        a=[''.join(p) for p in permutations(s1)]
        for i in a:
            if i in (s2):
                return True
        return False
        