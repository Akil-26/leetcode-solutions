class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        k =  len(colors)
        for i in range(k):
            if (colors[i] ^ colors[-1]) | (colors[-1-i] ^ colors[0]):
                return k-1-i
        return 0