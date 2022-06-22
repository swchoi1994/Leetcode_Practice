class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        i = len(nums)-k
        return nums[i]