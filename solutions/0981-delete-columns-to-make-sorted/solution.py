class Solution:
    def minDeletionSize(self, a: List[str]) -> int:
        return sum([*q]>sorted(q) for q in zip(*a))
