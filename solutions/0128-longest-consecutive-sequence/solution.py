class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        lo = 0
        for n in sett:
            if (n-1) not in sett:
                le = 1
                while (n+le) in sett:
                    le += 1
                lo = max(le, lo)
        return lo
