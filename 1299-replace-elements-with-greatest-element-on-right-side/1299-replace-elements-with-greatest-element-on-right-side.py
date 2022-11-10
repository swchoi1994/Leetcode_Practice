class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        # reverse iteration
        # new max = max(oldmax, arr[i])
        
        
        arrMax = -1
        
        for i in range(len(arr)-1,-1,-1):
            
            newMax = max(arrMax, arr[i])
            arr[i] = arrMax
            arrMax = newMax
        return arr