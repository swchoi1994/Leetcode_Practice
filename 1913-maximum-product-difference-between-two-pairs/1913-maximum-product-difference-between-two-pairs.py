class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        m,n = nums[0], nums[1]
        
        x, y = nums[-1], nums[-2]
        
        return (x*y) - (m*n)