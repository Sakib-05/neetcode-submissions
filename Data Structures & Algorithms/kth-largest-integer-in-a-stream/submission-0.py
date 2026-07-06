from heapq import *
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = []
        heapify(self.arr)
        for num in nums:
            heappush(self.arr, -num)

        

    def add(self, val: int) -> int:
        heappush(self.arr, -val)
        stack = []

        for i in range(self.k-1):
            stack.append(heappop(self.arr))
        
        res = -self.arr[0]

        while stack:
            heappush(self.arr,stack.pop())

        return res
    

    # 1,2,3,3,3,5,6,7

        
