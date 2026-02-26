class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        for i in range(len(s)-1,0,-1):
            if int(s[i]) + carry == 1:
                steps += 2
                carry = 1
            else:
                steps += 1
        return steps+carry

        """
        num = int(s,2)
        co = 0
        while num != 1:
            if num % 2 != 0:
                num+=1
                co+=1
            else:
                num//=2
                co+=1
        return co 
        """
