class Solution(object):
    def minCostConnectPoints(self, points):
        #forming edge
        N=len(points)
        adj={i:[] for i in range(N)}
        for i in range(N):
            x1,y1=points[i]
            for j in range(i+1,N):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        #prim's algo
        visit=set()
        res=0
        minH=[[0,0]]
        while len(visit)<N:
            cost,i= heapq.heappop(minH)
            if i in visit:
                continue
            visit.add(i)
            res+=cost
            for neiCost,nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH,[neiCost,nei])
        return res


        