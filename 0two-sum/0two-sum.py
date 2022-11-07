class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        
        for i, num in enumerate(nums):
            if target - num in seen_map:
                return [seen_map[target - num], i]
            seen_map[num] = i