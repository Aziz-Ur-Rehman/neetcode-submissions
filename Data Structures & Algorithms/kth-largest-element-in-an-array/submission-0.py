from heapq import heapify, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapify(nums)
        res = float("-inf")
        for _ in range(k):
            res = heappop(nums)
        return res *-1