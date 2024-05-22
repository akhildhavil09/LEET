class Solution(object):
    def partition(self, s):
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                partitions.append(path[:])
                return

            for end in range(start, len(s)):
                substring = s[start:end + 1]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end + 1, path)
                    path.pop()

        partitions = []
        backtrack(0, [])
        return partitions

