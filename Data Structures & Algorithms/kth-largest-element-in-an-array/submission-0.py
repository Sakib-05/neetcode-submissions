from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        print(nums)

        heapify(nums)
        print(nums)

        for x in range(k-1): heappop(nums)


        return -nums[0]

        