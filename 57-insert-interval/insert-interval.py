class Solution(object):
    def insert(self, intervals, newinterval):
        res=[]
        for i in range(len(intervals)):
            if newinterval[1]<intervals[i][0]:
                res.append(newinterval)
                return res+intervals[i:]
            elif newinterval[0]>intervals[i][1]:
                res.append(intervals[i])
            else:
                newinterval=[min(newinterval[0],intervals[i][0]),max(newinterval[1],intervals[i][1])]
        res.append(newinterval)
        return res