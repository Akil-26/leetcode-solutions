class Solution:
    def isValid(self, s: str) -> bool: 
        stack = []
        dic_val = {")":"(","}":"{","]":"["}
        for ch in s:
            if ch in dic_val:
                top = stack.pop() if stack else '#'
                if dic_val[ch] != top:
                    return False
            else:
                stack.append(ch)
        return not stack
