class Solution(object):
    def letterCombinations(self, digits):
        if not digits: return []
        mapping_dict={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        res=[]
        def dfs(index,path):
            if index==len(digits):
                res.append(''.join(path))
                return
            current_number= digits[index]
            for letter in mapping_dict[current_number]:
                path.append(letter)
                dfs(index+1,path)
                path.pop()
        dfs(0,[])
        return res