class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda i:i[1])
        count=0
        res=[]

        for i in intervals:
            if res and i[0] < res[-1][1]:
                count+=1
            else:
                res.append(i)
        return count

        