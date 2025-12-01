class Solution:
    def reverseBits(self, n: int) -> int:
        val = f'{n:032b}'
        res = val[::-1]
        return int(res,2)
