class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if (s1[0] == s2[0] and s2[2] == s1[2] and 
            (s1[1] != s2[3] or s1[3] != s2[1])):
            return False

        if (s1[1] == s2[1] and s2[3] == s1[3] and 
            (s1[0] != s2[2] or s1[2] != s2[0])):
            return False

        if (s1[0] == s2[0] and s2[2] == s1[2] and 
            (s1[1] == s2[3] and s1[3] == s2[1])):
            return True

        if (s1[1] == s2[1] and s2[3] == s1[3] and 
            (s1[0] == s2[2] and s1[2] == s2[0])):
            return True

        if (s1[0] == s2[2] and s2[0] == s1[2] and 
            s1[1] == s2[3] and s2[1] == s1[3]):
            return True

        return False
