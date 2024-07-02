class Solution(object):
    def partitionLabels(self, s):
        lastindex={}
        for i,c in enumerate (s):
            lastindex[c]=i
        res=[]
        size,end=0,0
        for i,c in enumerate (s):
            size+=1
            if lastindex[c]> end:
                end=lastindex[c]
            end= max(end, lastindex[c])

            if i==end:
                res.append(size)
                size=0
        return res
        