class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {"}":"{",")":"(","]":"["}
        for i in s:
            if i in dic:
                if stack and stack[-1] == dic[i]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(i)
        return True if not stack else False