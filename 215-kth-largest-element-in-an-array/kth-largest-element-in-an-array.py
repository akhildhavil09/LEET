class Solution(object):
    def findKthLargest(self, nums, k):
        heap=[]
        for num in nums:
            if len(heap)<k:
                heapq.heappush(heap,num)
            else:
                heapq.heappushpop(heap,num)
        return heap[0]        