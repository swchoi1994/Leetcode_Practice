class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSub = 0
        
        for i in nums:
            if currSub < 0:
                currSub = 0
            currSub += i
            maxSub = max(maxSub, currSub)
        return maxSub