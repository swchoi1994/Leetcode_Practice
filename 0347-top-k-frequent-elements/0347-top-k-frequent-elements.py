from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        count = Counter(nums)
        
        return list(zip(*count.most_common(k)))[0]
    
