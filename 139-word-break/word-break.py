class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo={}
        def helper(index):
            if index==len(s):
                return True
            if index in memo:
                return memo[index]

            for word in wordDict:
                if index+ len(word)> len(s):
                    continue
                
                if s[index: index+ len(word)]== word:

                    if helper(index+len(word)):
                        memo[index]= True
                        return True
            
            memo[index]= False
            return False
        
        return helper(0)