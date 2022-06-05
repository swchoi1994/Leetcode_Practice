class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_string_builder = []
        
        # Remember that we want to loop backward through the string.
        for char in reversed(num):
            if char in {'0', '1', '8'}:
                rotated_string_builder.append(char)
            elif char == '6':
                rotated_string_builder.append('9')
            elif char == '9':
                rotated_string_builder.append('6')
            else: # This must be an invalid digit.
                return False
        
        # In Python, we convert a list of characters to
        # a string using join.
        rotated_string = "".join(rotated_string_builder)
        return rotated_string == num