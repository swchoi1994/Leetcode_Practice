class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        
        for string in s:
            if string not in pairs:
                stack.append(string)
            elif not stack or stack.pop() != pairs[string]:
                return False
            
        return len(stack) == 0