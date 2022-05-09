'''
TC - nlogn
SC - O(1) or logn
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n, heap = len(nums), []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
        
        
        