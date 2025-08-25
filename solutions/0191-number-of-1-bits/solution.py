import re
class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        bina = bin(n)
        for i in range(len(bina)):

            if bina[i] == "1":
                sum +=1
            else:
                continue
        return sum






