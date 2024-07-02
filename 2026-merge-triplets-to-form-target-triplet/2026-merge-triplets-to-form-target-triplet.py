class Solution(object):
    def mergeTriplets(self, triplets, target):
        x,y,z= target
        xstatus=ystatus=zstatus= False

        for triplet in triplets:
            a,b,c= triplet
            if a<=x and b<=y and c<=z:
                if a==x:
                    xstatus=True
                if b==y:
                    ystatus= True
                if c==z:
                    zstatus= True
        return xstatus and ystatus and zstatus
        