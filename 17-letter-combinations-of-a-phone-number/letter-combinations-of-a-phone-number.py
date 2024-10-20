class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        maap={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        res=[]

        def helper(index,path):
            if index==len(digits):
                res.append(''.join(path))
                return

            cur_num= digits[index]
            for letter in maap[cur_num]:
                path.append(letter)
                helper(index+1,path)
                path.pop()
        helper(0,[])
        return res