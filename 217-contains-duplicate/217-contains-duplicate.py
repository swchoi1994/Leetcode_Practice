class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = set()
        
        for i in nums:
            if i in hashMap:
                return True
            hashMap.add(i)
        return False