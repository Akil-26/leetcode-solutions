class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n  = len(operations)
        length = 1
        for _  in range(n):
            length *= 2
        shift = 0
        for i in range(n-1,-1,-1):
            half = length // 2
            if k > half:
                k -= half
                if operations[i] == 1:
                    shift += 1
            length = half
        return chr((ord('a') - ord('a') + shift) % 26 + ord('a'))
