class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bits = bin(n)[2:]
        res = ''
        for i in bits:
            res += str(int(i) ^ 1)
        return int(res,2)
