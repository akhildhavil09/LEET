class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtrack(index, prev_num, curr_result, expression):
            # Think: If we've used all digits and got target, we found a valid expression
            if index == len(num):
                if curr_result == target:
                    result.append(expression)
                return
            
            # Think: Try different length numbers starting at current index
            for i in range(index, len(num)):
                # Think: Skip numbers with leading zeros
                if i != index and num[index] == '0':
                    break
                    
                # Think: Get the current number we're considering
                curr_num = int(num[index:i + 1])
                
                if index == 0:
                    # Think: First number, no operator needed
                    backtrack(i + 1, curr_num, curr_num, str(curr_num))
                else:
                    # Think: Try addition
                    backtrack(i + 1, curr_num, curr_result + curr_num, 
                            expression + '+' + str(curr_num))
                    
                    # Think: Try subtraction
                    backtrack(i + 1, -curr_num, curr_result - curr_num, 
                            expression + '-' + str(curr_num))
                    
                    # Think: Try multiplication
                    # For multiplication, we need to subtract the previous number
                    # and add the product of previous and current number
                    backtrack(i + 1, prev_num * curr_num,
                            curr_result - prev_num + (prev_num * curr_num),
                            expression + '*' + str(curr_num))
        
        result = []
        if not num:
            return result
        backtrack(0, 0, 0, "")
        return result