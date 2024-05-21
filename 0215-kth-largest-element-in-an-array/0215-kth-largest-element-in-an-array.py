import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        heap = nums[:k]  # Take the first k elements
        heapq.heapify(heap)  # Create a min-heap

        for num in nums[k:]:  # Iterate through the rest of nums
            if num > heap[0]:  # If the current number is larger than the smallest in the heap
                heapq.heappop(heap)  # Remove the smallest
                heapq.heappush(heap, num)  # Push the current number into the heap

        return heap[0]