from heapq import heapify, heappop
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        heapify(nums)

        res = 1
        last = heappop(nums)
        maxx = 1

        while nums:

            hold = heappop(nums)
            if hold-last == 1:
                maxx += 1
            elif hold-last == 0:
                pass
            else:
                print(maxx)
                res = max(res,maxx)
                maxx = 1
            
            res = max(res,maxx)
            last = hold
        return res
            


