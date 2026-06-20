class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = {}

        for num in nums:
            if count_map.get(num):
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        for num, count in count_map.items():
            if count>1:
                return True
        return False