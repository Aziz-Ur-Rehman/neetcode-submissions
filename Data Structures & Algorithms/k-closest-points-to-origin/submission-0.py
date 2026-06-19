import math
from heapq import heapify, heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in points:
            dist = math.sqrt(i[0]**2+i[1]**2)
            minHeap.append([dist,i[0],i[1]])

        heapify(minHeap)

        res = []
        for _ in range(k):
            d,x,y = heappop(minHeap)
            res.append([x,y])
        return res