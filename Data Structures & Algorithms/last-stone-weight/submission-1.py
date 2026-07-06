from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        print(stones)
        heapify(stones)
        print(stones)

        while len(stones) > 1:
            x = -heappop(stones)
            y = -heappop(stones)

            if x > y:
                new = x-y
                heappush(stones,-new)
            # else:
            #     new = x - y
            #     heappush(stones,-new)


        if len(stones) ==1:
            return -stones[0]




        return 0

        