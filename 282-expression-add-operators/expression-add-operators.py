class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtrack(index, prev_num, running_res, exp):
            if index==len(num):
                if running_res==target:
                    res.append(exp)
                return
            
            for i in range(index,len(num)):
                if i!=index and num[index]=='0':
                    break
                cur_num= int(num[index:i+1])

                if index==0:
                    backtrack(i+1, cur_num, cur_num, str(cur_num))
                else:
                    backtrack(i+1,cur_num, running_res+cur_num, exp+'+'+str(cur_num))

                    backtrack(i+1, -cur_num, running_res-cur_num, exp+'-'+str(cur_num))

                    backtrack(i+1,prev_num*cur_num, running_res- prev_num +(prev_num*cur_num), exp+'*'+str(cur_num))
        res=[]
        if not num:
            return res
        backtrack(0,0,0,"")
        return res