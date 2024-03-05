class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        ans = 0
        
        for i in range(len(nums)):
            ans += nums[i]
            res[i] = ans
        return res