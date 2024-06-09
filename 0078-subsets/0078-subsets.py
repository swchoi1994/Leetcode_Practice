class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        
        currentSubsets = []
        
        def dfs(index):
            if index >= len(nums):
                allSubsets.append(currentSubsets[:])
                return
            
            currentSubsets.append(nums[index])
            dfs(index + 1)
            
            currentSubsets.pop()
            dfs(index + 1)
        
        dfs(0)
        
        return allSubsets