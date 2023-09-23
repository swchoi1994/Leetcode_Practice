class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a

        
        # if n <= 3:
        #     return n
        # n1, n2 = 2, 3
        
        # for i in range(4, n+1):
        #     tmp = n1 + n2
        #     n1 = n2
        #     n2 = tmp
        # return n2