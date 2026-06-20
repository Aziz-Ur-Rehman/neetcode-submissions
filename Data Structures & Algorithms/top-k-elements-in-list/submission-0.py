from heapq import heapify, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if freq.get(num) is None:
                freq[num] = 1
            else:
                freq[num] += 1

        temp_list = [(-1*j, i) for i,j in freq.items()]
        heapify(temp_list)

        res = []
        for _ in range(k):
            res.append(heappop(temp_list)[1])

        return res