from heapq import heapify, heappop,heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]
        stones = [-stone for stone in stones]
        heapify(stones)
        while len(stones) > 1:
            print(stones)
            hold1 = heappop(stones)
            hold2 = heappop(stones)

            if min(hold1,hold2)-max(hold1,hold2) < 0:
                heappush(stones, min(hold1,hold2)-max(hold1,hold2))

        if len(stones)>0:
            return -1*heappop(stones)
        else:
            return 0