class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}

        for i, j in enumerate(nums):
            if diff_map.get(target - j) is None:
                diff_map[j] = i
            else:
                return [diff_map[target - j], i]