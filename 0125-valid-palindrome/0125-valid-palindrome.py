class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char.isalnum():
                stack.append(char.lower())
        
        while len(stack)>1:
            if stack.pop() != stack.pop(0):
                return False
        return True