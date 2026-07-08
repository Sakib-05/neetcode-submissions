from math import *
from heapq import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distance = lambda point: sqrt(pow(point[0],2) + pow(point[1],2))

        heap = []
        heapify(heap)

        for point in points:
            heappush(heap, (distance(point),point))

            

        print(heap)

        res = []

        while heap and len(res) <k:
            point = heappop(heap)[1]

            res.append(point)



        return res
        