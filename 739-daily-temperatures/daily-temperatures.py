class Solution(object):
    def dailyTemperatures(self, temp):
        stack=[]
        res=[0]*len(temp)
        for index in range(len(temp)):
            while stack and temp[index]> temp[stack[-1]]:
                prev_index= stack.pop()
                res[prev_index]= index-prev_index
            stack.append(index)
        return res