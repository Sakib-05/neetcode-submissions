from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        heapify(minheap)

        for num in nums:
            heappush(minheap, num)

            if len(minheap)>k:
                heappop(minheap)
        print(minheap)
        
        
        return minheap[0]
        