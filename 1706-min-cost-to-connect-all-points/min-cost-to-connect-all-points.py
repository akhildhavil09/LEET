class Solution(object):
    def minCostConnectPoints(self, points):
        n=len(points)
        adj={i:[] for i in range(n)}

        for i in range(n):
            x,y= points[i]
            for j in range(i+1,n):
                p,q= points[j]

                dist= abs(x-p)+abs(y-q)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        
        #prim's
        visit=set()
        res=0
        minh=[[0,0]]

        while len(visit)<n:
            cost,i= heapq.heappop(minh)
            if i in visit:
                continue
            res+=cost
            visit.add(i)
            for neiCost,nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minh,[neiCost,nei])
        return res