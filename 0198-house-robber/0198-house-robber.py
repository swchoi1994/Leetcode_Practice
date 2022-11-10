class Solution:
    def rob(self, nums: List[int]) -> int:
        # need to use tabulation
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        rob1, rob2 = 0, 0
        
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2