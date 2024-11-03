class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtrack( index, prev_num, cur_res, expression):
            if index==len(num):
                if cur_res==target:
                    result.append(expression)
                return

            for i in range(index, len(num)):
                if i!=index and num[index]=='0':
                    break
                
                cur_num= int(num[index:i+1])

                if index==0:
                    backtrack(i+1, cur_num, cur_num, str(cur_num))
                else:
                    #addition
                    backtrack(i+1, cur_num, cur_res+cur_num, expression+ '+' +str(cur_num))
                    #subtraction
                    backtrack(i+1, -cur_num, cur_res-cur_num, expression+ '-' +str(cur_num))
                    #multiplication
                    backtrack(i+1, prev_num*cur_num, cur_res-prev_num +(prev_num*cur_num), expression+ '*' + str(cur_num))
        result=[]
        if not num: return result
        backtrack(0,0,0,"")
        return result