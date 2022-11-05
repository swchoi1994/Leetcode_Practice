class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        dict_t = Counter(t)
        
        required = len(dict_t)
        
        l_pointer, r_pointer = 0,0
        
        unique_num_formed = 0
        
        window_counts = {}
        
        ans = float("inf"), None, None
        
        while r_pointer < len(s):
            character = s[r_pointer]
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in dict_t and window_counts[character] == dict_t[character]:
                unique_num_formed += 1
            
            while l_pointer <= r_pointer and unique_num_formed == required:
                character = s[l_pointer]
                
                if r_pointer - l_pointer + 1 < ans[0]:
                    ans = (r_pointer - l_pointer+1, l_pointer, r_pointer)
                    
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    unique_num_formed -= 1
                
                l_pointer +=1
            r_pointer += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]