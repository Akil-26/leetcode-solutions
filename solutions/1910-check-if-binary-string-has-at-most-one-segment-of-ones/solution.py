class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        """seen = False
        for i in s:
            if i == "0":
                seen = True
            elif seen:
                return False
        return True"""
        return "01" not in s
