class Solution(object):
    def kClosest(self, points, k):
        def eud(point):
            x,y= point
            distance= x**2+y**2
            return distance
        maxheap=[]
        for point in points:
            distance=eud(point)
            heapq.heappush(maxheap,(-distance,point))

            if len(maxheap)>k:
                heapq.heappop(maxheap)
        
        return [point for (_,point) in maxheap]