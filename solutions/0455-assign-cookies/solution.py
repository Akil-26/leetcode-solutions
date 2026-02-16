class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        i=0
        j=0
        s=sorted(s)
        g=sorted(g)
        goals=0
        while(i<len(g) and len(s)>j):
            if(g[i]<=s[j]):
                goals+=1
                i+=1
                j+=1
            else:
                j+=1
        return goals
