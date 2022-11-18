class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                
                # save the topLeft
                topLeft = matrix[top][l + i]
                
                # move bottom Left into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                # move top left into 
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                
                matrix[bottom][r - i] = matrix[top + i][r]
                
                matrix[top + i][r] = topLeft
                
            
            l += 1
            r -= 1